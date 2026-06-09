---
id: "wwdc2021-10190"
event: "wwdc2021"
year: 2021
title: "Create audio drivers with DriverKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10190"
topics: ["System Services", "Audio & Video"]
platforms: ["macOS"]
hasTranscript: true
---

# Create audio drivers with DriverKit

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10190](https://developer.apple.com/videos/play/wwdc2021/10190)

Discover how to use the AudioDriverKit API to consolidate your Audio Server plug-in and DriverKit extension into a single package. Learn how you can simplify audio driver installation with an app instead of an installer package and distribute your driver through the Mac App Store. And we’ll take you through how the Core Audio HAL interacts with AudioDriverKit and discover best practices for audio device drivers.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,753 words)

## Code Snippets

### Subclass of IOUserAudioDriver — [5:58]

```objectivec
// SimpleAudioDriver example, subclass of IOUserAudioDriver

class SimpleAudioDriver: public IOUserAudioDriver
{
public:
	virtual bool init() override;
	virtual void free() override;

	virtual kern_return_t Start(IOService* provider) override;	
	virtual kern_return_t Stop(IOService* provider) override;
	virtual kern_return_t NewUserClient(uint32_t in_type,
										 IOUserClient** out_user_client) override;

	virtual kern_return_t StartDevice(IOUserAudioObjectID in_object_id,
									   IOUserAudioStartStopFlags in_flags) override;

	virtual kern_return_t StopDevice(IOUserAudioObjectID in_object_id,
									  IOUserAudioStartStopFlags in_flags) override;
```

### Override of IOService::NewUserClient — [6:27]

```objectivec
// SimpleAudioDriver example override of IOService::NewUserClient
kern_return_t SimpleAudioDriver::NewUserClient_Impl(uint32_t in_type,
													 IOUserClient** out_user_client)
{
	kern_return_t error = kIOReturnSuccess;
	//	Have the super class create the IOUserAudioDriverUserClient object if the type is
	//	kIOUserAudioDriverUserClientType
	if (in_type == kIOUserAudioDriverUserClientType)
	{
		error = super::NewUserClient(in_type, out_user_client, SUPERDISPATCH);
	}
	else
	{
		IOService* user_client_service = nullptr;
		error = Create(this, "SimpleAudioDriverUserClientProperties", &user_client_service);
		FailIfError(error, , Failure, "failed to create the SimpleAudioDriver user-client");
		*out_user_client = OSDynamicCast(IOUserClient, user_client_service);
	}
	return error;
}
```

### SimpleAudioDevice::init — [7:04]

```objectivec
// SimpleAudioDevice::init, set device sample rates and create IOUserAudioStream object
...
    SetAvailableSampleRates(sample_rates, 2); 
    SetSampleRate(kSampleRate_1);

    //	Create the IOBufferMemoryDescriptor ring buffer for the input stream
    OSSharedPtr<IOBufferMemoryDescriptor> io_ring_buffer;
    const auto buffer_size_bytes = static_cast<uint32_t>(in_zero_timestamp_period *  
        sizeof(uint16_t) * input_channels_per_frame);
    IOBufferMemoryDescriptor::Create(kIOMemoryDirectionInOut, buffer_size_bytes, 0, 
       io_ring_buffer.attach());

    //	Create input stream object and pass in the IO ring buffer memory descriptor
    ivars->m_input_stream = IOUserAudioStream::Create(in_driver, 
                                                      IOUserAudioStreamDirection::Input, 
                                                      io_ring_buffer.get());
...
```

### SimpleAudioDevice::init continued — [8:19]

```objectivec
// SimpleAudioDevice::init continued
    IOUserAudioStreamBasicDescription input_stream_formats[2] = {
            kSampleRate_1, IOUserAudioFormatID::LinearPCM,
            static_cast<IOUserAudioFormatFlags>(
                    IOUserAudioFormatFlags::FormatFlagIsSignedInteger | 
                    IOUserAudioFormatFlags::FormatFlagsNativeEndian),
            static_cast<uint32_t>(sizeof(int16_t)*input_channels_per_frame),
            1,
            static_cast<uint32_t>(sizeof(int16_t)*input_channels_per_frame),
            static_cast<uint32_t>(input_channels_per_frame),
            16
		    },
        ...
    }

    ivars->m_input_stream->SetAvailableStreamFormats(input_stream_formats, 2);
    ivars->m_input_stream_format = input_stream_formats[0];
    ivars->m_input_stream->SetCurrentStreamFormat(&ivars->m_input_stream_format);

    error = AddStream(ivars->m_input_stream.get());
```

### Create a input volume level control object — [8:50]

```objectivec
//	Create volume control object for the input stream.
ivars->m_input_volume_control = IOUserAudioLevelControl::Create(in_driver,
    true, -6.0, {-96.0, 0.0},
    IOUserAudioObjectPropertyElementMain,
    IOUserAudioObjectPropertyScope::Input,
    IOUserAudioClassID::VolumeControl);

//	Add volume control to device
error = AddControl(ivars->m_input_volume_control.get());
```

### Create custom property — [9:22]

```objectivec
// SimpleAudioDevice::init, Create custom property

IOUserAudioObjectPropertyAddress prop_addr = {
    kSimpleAudioDriverCustomPropertySelector,
    IOUserAudioObjectPropertyScope::Global,
    IOUserAudioObjectPropertyElementMain
};

custom_property = IOUserAudioCustomProperty::Create(in_driver, prop_addr, true,
    IOUserAudioCustomPropertyDataType::String,
    IOUserAudioCustomPropertyDataType::String);

qualifier = OSSharedPtr(
    OSString::withCString(kSimpleAudioDriverCustomPropertyQualifier0), OSNoRetain);
data = OSSharedPtr(
    OSString::withCString(kSimpleAudioDriverCustomPropertyDataValue0), OSNoRetain);
custom_property->SetQualifierAndDataValue(qualifier.get(), data.get());

AddCustomProperty(custom_property.get());
```

### Subclass of IOUserAudioDevice — [10:47]

```objectivec
// SimpleAudioDevice example subclass of IOUserAudioDevice

class SimpleAudioDevice: public IOUserAudioDevice
{
...
    virtual kern_return_t StartIO(IOUserAudioStartStopFlags in_flags) final LOCALONLY;
    virtual kern_return_t StopIO(IOUserAudioStartStopFlags in_flags) final LOCALONLY;

private:
    kern_return_t StartTimers() LOCALONLY;
    void StopTimers() LOCALONLY;
    void UpdateTimers() LOCALONLY;
    virtual void ZtsTimerOccurred(OSAction* action,
								   uint64_t time) TYPE(IOTimerDispatchSource::TimerOccurred);
    virtual void ToneTimerOccurred(OSAction* action,
									uint64_t time) TYPE(IOTimerDispatchSource::TimerOccurred);
    void GenerateToneForInput(size_t in_frame_size) LOCALONLY;
}
```

### StartIO — [11:18]

```objectivec
// StartIO 
kern_return_t SimpleAudioDevice::StartIO(IOUserAudioStartStopFlags in_flags)
{
    __block kern_return_t error = kIOReturnSuccess;
    __block OSSharedPtr<IOMemoryDescriptor> input_iomd;
    ivars->m_work_queue->DispatchSync(^(){
		//	Tell IOUserAudioObject base class to start IO for the device
        error = super::StartIO(in_flags);
        if (error == kIOReturnSuccess)
        {
            // Get stream IOMemoryDescriptor, create mapping and store to ivars	
            input_iomd = ivars->m_input_stream->GetIOMemoryDescriptor();
            input_iomd->CreateMapping(0, 0, 0, 0, 0, ivars->m_input_memory_map.attach());

            // Start timers to send timestamps and generate sine tone on the stream buffer	
            StartTimers();
        }
    });
    return error;
}
```

### StartTimers — [11:57]

```objectivec
kern_return_t SimpleAudioDevice::StartTimers()
{
...
	//	clear the device's timestamps
	UpdateCurrentZeroTimestamp(0, 0);
	auto current_time = mach_absolute_time();
	auto wake_time = current_time + ivars->m_zts_host_ticks_per_buffer;

	//	start the timer, the first time stamp will be taken when it goes off
	ivars->m_zts_timer_event_source->WakeAtTime(kIOTimerClockMachAbsoluteTime,
												 wake_time,
												 0);
	ivars->m_zts_timer_event_source->SetEnable(true);
...
}
```

### ZtsTimerOccurred — [12:27]

```objectivec
void SimpleAudioDevice::ZtsTimerOccurred_Impl(OSAction* action, uint64_t time)
{
...
	GetCurrentZeroTimestamp(&current_sample_time, &current_host_time);
	auto host_ticks_per_buffer = ivars->m_zts_host_ticks_per_buffer;
	if (current_host_time != 0) {
		current_sample_time += GetZeroTimestampPeriod();
		current_host_time += host_ticks_per_buffer;
	}
	else {
		current_sample_time = 0;
		current_host_time = time;
	}
	// Update the device with the current timestamp
	UpdateCurrentZeroTimestamp(current_sample_time, current_host_time);

	//	set the timer to go off in one buffer
	ivars->m_zts_timer_event_source->WakeAtTime(kIOTimerClockMachAbsoluteTime,
												current_host_time + host_ticks_per_buffer, 0);
}
```

### GenerateToneForInput — [13:03]

```objectivec
void SimpleAudioDevice::GenerateToneForInput(size_t in_frame_size) 
{
	// Fill out the input buffer with a sine tone
	if (ivars->m_input_memory_map)
	{
		//	Get the pointer to the IO buffer and use stream format information
		//	to get buffer length
		const auto& format = ivars->m_input_stream_format;
		auto buffer_length = ivars->m_input_memory_map->GetLength() / 
            (format.mBytesPerFrame / format.mChannelsPerFrame);
		auto num_samples = in_frame_size;
		auto buffer = reinterpret_cast<int16_t*>(ivars->m_input_memory_map->GetAddress() +  
            ivars->m_input_memory_map->GetOffset());
...	
}
```

### GenerateToneForInput continued — [13:30]

```objectivec
void SimpleAudioDevice::GenerateToneForInput(size_t in_frame_size) 
{
...
	auto input_volume_level = ivars->m_input_volume_control->GetScalarValue();

	for (size_t i = 0; i < num_samples; i++)
	{
		float float_value = input_volume_level * 
    sin(2.0 * M_PI * frequency * 
       static_cast<double>(ivars->m_tone_sample_index) / format.mSampleRate);

		int16_t integer_value = FloatToInt16(float_value);
		for (auto ch_index = 0; ch_index < format.mChannelsPerFrame; ch_index++)
		{
			auto buffer_index =
                (format.mChannelsPerFrame * ivars->m_tone_sample_index + ch_index) %         
                buffer_length;
			buffer[buffer_index] = integer_value;
		}
		ivars->m_tone_sample_index += 1;
	}
}
```

### IOUserAudioClockDevice.h and IOUserAudioDevice.h — [14:02]

```objectivec
// IOUserAudioClockDevice.h and IOUserAudioDevice.h

kern_return_t RequestDeviceConfigurationChange(uint64_t in_change_action,
											    OSObject* in_change_info);

virtual kern_return_t PerformDeviceConfigurationChange(uint64_t in_change_action,
											            OSObject* in_change_info);

virtual kern_return_t AbortDeviceConfigurationChange(uint64_t change_action,
													  OSObject* in_change_info);
```

### HandleTestConfigChange — [15:32]

```objectivec
kern_return_t SimpleAudioDriver::HandleTestConfigChange()
{
	auto change_info = OSSharedPtr(OSString::withCString("Toggle Sample Rate"), OSNoRetain);
	return ivars->m_simple_audio_device->RequestDeviceConfigurationChange(
        k_custom_config_change_action, change_info.get());
}

class SimpleAudioDevice: public IOUserAudioDevice
{
...
	virtual kern_return_t PerformDeviceConfigurationChange(uint64_t change_action,
												    OSObject* in_change_info) final LOCALONLY;
}
```

### PerformDeviceConfigurationChange — [16:05]

```objectivec
// In SimpleAudioDevice::PerformDeviceConfigurationChange
	kern_return_t ret = kIOReturnSuccess;
	switch (change_action) {
		case k_custom_config_change_action: {
			if (in_change_info)	{
				auto change_info_string = OSDynamicCast(OSString, in_change_info);
				DebugMsg("%s", change_info_string->getCStringNoCopy());
			}

			double rate_to_set = static_cast<uint64_t>(GetSampleRate()) != 
                static_cast<uint64_t>(kSampleRate_1) ? kSampleRate_1 : kSampleRate_2;
			ret = SetSampleRate(rate_to_set);
			if (ret == kIOReturnSuccess) {
				// Update stream formats with the new rate
				ret = ivars->m_input_stream->DeviceSampleRateChanged(rate_to_set);
			}
		}
			break;

		default:
			ret = super::PerformDeviceConfigurationChange(change_action, in_change_info);
			break;
	}

	// Update the cached format:
	ivars->m_input_stream_format = ivars->m_input_stream->GetCurrentStreamFormat();

	return ret;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10190/5/C1305D2C-3534-4C07-A3D7-3A70DA9FCAE2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10190/5/C1305D2C-3534-4C07-A3D7-3A70DA9FCAE2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10190) — developer.apple.com. Indexed for agent consumption._