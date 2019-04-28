Readme.txt
 
-------------------------------------------------------------------
This file outlines changes since the last release of MIBs.
 
It is very strongly recommended that you load and compile ALL of
the MIBs provided.
 
Please load the 'hpicfOid.mib' before loading the other specific
MIBs.  This is due to the fact that the 'hpicfOid.mib' is the
parent MIB to most of the HP device specific MIBs.
-------------------------------------------------------------------

        hpicfAMPServer.mib
           -new objects
            hpicfArubaVPNBkpIP
            hpicfArubaVPNBkpIPType

        hpicfAuth.mib
           -new objects
            hpSwitchFpsPasswordClear
            hpSwitchFpsFactoryReset
            hpSwitchFpsPasswordRecovery
            hpSwitchFpsDiagnosticResetClearButton
            hpSwitchFpsDiagnosticResetSerialConsole
            hpSwitchFpsDisplayInConfig
            hpSwitchAuthenCachedReauthAuthorized
            hpSwitchRadiusDeadTimeInfinite
            hpSwitchRadiusTrackingInterval

        hpicfBasic.mib
           -new objects
            hpicfBasicLogPerIpFilterAction
            hpicfBasicLogPerIpFilterEntry
            hpicfBasicLogPerIpFilterEventList
            hpicfBasicLogPerIpFilterRowStatus
            hpicfBasicLogPerIpFilterSeverity
            hpicfBasicLogPerIpFiltersTable
            hpicfBasicLogPerIpFilterSysModule
            hpicfBasicLogPerIpFilterType
            hpicfBasicLogPerIpIndex
 
        hpicfConfig.mib
           -new mib
 
        hpicfDebugLog.mib
           -new objects
            hpicfDebugTimeStamp
 
        hpicfDevConf.mib
           -new objects
            hpSwitchProfTunneledNodeSupport

        hpicfDipldv6.mib
           -new mib

        hpicfDot1x.mib
           -modified objects
            hpicfDot1xSMAuthPaeState
             
           -new objects
            hpicfDot1xPaePortCritAuthVoiceVid
            hpicfDot1xPaePortCritAuthDataVid
            hpicfDot1xPaePortCritAuthUserRole
            hpicfDot1xPaePortOpenAuthVoiceVid
            hpicfDot1xPaePortOpenAuthDataVid
            hpicfDot1xPaePortOpenAuthUserRole
            hpicfDot1xPaePortInitialRole
            hpicfDot1xAuthEnforceCacheReauth

        hpicfDSnoopV6.mib
           -new mib

        hpicfGenericVlan.mib
           -new objects
            hpicfDot1qTpFdbInstalledTime

        hpicfLma.mib
           -new objects
            hpicfLmaMacPin

        hpicfNtp.mib 
           -new objects
            hpicfNtpInetServerNameTable
            hpicfNtpInetServerNameEntry
            hpicfNtpServerNameIndex
            hpicfNtpInetServerName
            hpicfNtpInetServerNameRowStatus
            hpicfNtpServerNameResolvAddType
            hpicfNtpServerNameResolvAddress
            hpicfNtpServerNameResolveStatus
            hpicfNtpInetServerNameAuthKeyId
            hpicfNtpConfigServerNamePollMinInterval
            hpicfNtpConfigServerNamePollMaxInterval
            hpicfNtpServerNameAssoBurst
            hpicfNtpServerNameAssoIsOobm

        hpicfOid.mib
           -new objects
            arubaModuleJL557A
            arubaModuleJL558A
            arubaModuleJL559A
            arubaSwitchJL557A
            arubaSwitchJL558A
            arubaSwitchJL559A
 
        hpicfOpenFlow.mib
           -new objects
            hpicfOpenFlowControllerSourceAddressType
            hpicfOpenFlowControllerSourceAddress

        hpicfOspf.mib
           -new objects
            hpicfOspfIfFlagValue
            hpicfOspfIfMetricEntry
            hpicfOspfIfMetricTable
            hpicfOspfReferenceCost
  
        hpicfOspfv3.mib
           -new objects
            hpicfOspfv3IfFlagValue
            hpicfOspfv3IfMetricEntry
            hpicfOspfv3IfMetricTable
            hpicfOspfv3ReferenceCost
 
        hpicfPim6.mib
           -new mib

        hpicfRateLimit.mib
           -modified objects
            hpUnknownUnicastLimitPortSingleControlKbps

        hpicfRpvst.mib
           -new objects
            hpicfRpvstPortIeeeRstBpdu
        
        hpicfSavi.mib 
           -new mib

        hpicfSrcIp.mib
           -modified objects
            hpicfSrcIpProtocolIndex

        hpicfSyslog.mib
           -modified objects
            HpicfSyslogSystemModule

           -new objects
            hpicfSyslogControlFilterName
 
        hpicfUdpForward.mib
           -modified objects
            hpicfUdpFwdDhcpRelayAdminStatus

        hpicfUsrAuth.mib
           -modified objects
            hpicfUsrAuthWebAuthSessionState
            hpicfUsrAuthMacAuthSessionState

           -new objects
            hpicfUsrAuthMacPin 
            hpicfMacAuthRetainUnauthClients

        hpSwitchConfig.mib
           -new objects
            hpicfSwitchCLIOptimization
            hpSwitchPortNetworkDevice
   
        hpSwitchTrap.mib
           -new objects
            arubaSwitchJL557Atrap
            arubaSwitchJL558Atrap
            arubaSwitchJL559Atrap
 
 
List of new traps supported in this release
-------------------------------------------
        
         hpicfDipldv6.mib
            -new Trap objects
             hpicfDIPDv6SourceBindingOutOfResources
             hpicfDIPLDv6SourceBindingVoilations

         hpicfDSnoopV6.mib
            -new Trap objects
             hpicfDSnoopV6SourceBindingOutOfResources
             hpicfDSnoopV6SourceBindingErrantReply

         hpicfPim6.mib
            -new Trap objects
             hpicfPim6NeighborLoss
             hpicfPim6HardMRTFull
             hpicfPim6SoftMRTFull

