#
# PySNMP MIB module ASCEND-MIBL2TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBL2TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, NotificationType, ModuleIdentity, ObjectIdentity, iso, Counter64, MibIdentifier, Gauge32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtunnelServer = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 91))
mibl2TunnelGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 90))
mibtunnelServerTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 91, 1), )
if mibBuilder.loadTexts: mibtunnelServerTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibtunnelServerTable.setDescription('A list of mibtunnelServer profile entries.')
mibtunnelServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1), ).setIndexNames((0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-ServerEndpoint"))
if mibBuilder.loadTexts: mibtunnelServerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibtunnelServerEntry.setDescription('A mibtunnelServer entry containing objects that maps to the parameters of mibtunnelServer profile.')
tunnelServer_ServerEndpoint = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 1), DisplayString()).setLabel("tunnelServer-ServerEndpoint").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelServer_ServerEndpoint.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_ServerEndpoint.setDescription("The name of the remote tunnel endpoint. It should be the hostname or IP address that identifies the remote tunnel server, as required by the specific tunnel protocol. Usually, it matches the 'Tunnel-Server-Endpoint' RADIUS attribute but it may be different.")
tunnelServer_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("tunnelServer-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_Enabled.setDescription("A tunnel server can be disabled by setting this field to 'no'.")
tunnelServer_SharedSecret = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 3), DisplayString()).setLabel("tunnelServer-SharedSecret").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_SharedSecret.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_SharedSecret.setDescription('The shared secret (password) needed to bring up an L2TP Control Channel or an L2F tunnel with this server.')
tunnelServer_MaxClients = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 4), Integer32()).setLabel("tunnelServer-MaxClients").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_MaxClients.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_MaxClients.setDescription('The maximum number of clients that this tunnel may carry.')
tunnelServer_ValidCallTypes = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("allCalls", 1), ("analogCalls", 2), ("digitalCalls", 3)))).setLabel("tunnelServer-ValidCallTypes").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_ValidCallTypes.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_ValidCallTypes.setDescription('The valid call types that can be carried on this tunnel.')
tunnelServer_IpsecProfile = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 6), DisplayString()).setLabel("tunnelServer-IpsecProfile").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_IpsecProfile.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_IpsecProfile.setDescription('Name of the ipsec profile which should be used to build the IPSec Scheme for the IP Packets sent and received from this server.')
tunnelServer_ClientAuthId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 7), DisplayString()).setLabel("tunnelServer-ClientAuthId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_ClientAuthId.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_ClientAuthId.setDescription('The system name used by the Tunnel Initiator during Tunnel establishment for the purposes of tunnel authentication. This is different and independent from user authentication. In L2TP, this name is sent on the SCCRQ command. Used on L2TP and L2F.')
tunnelServer_ServerAuthId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 8), DisplayString()).setLabel("tunnelServer-ServerAuthId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_ServerAuthId.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_ServerAuthId.setDescription('The system name used by the Tunnel Terminator during Tunnel establishment for the purposes of tunnel authentication. This is different and independent from user authentication. In L2TP, this name is sent on the SCCRP command. Used on L2TP and L2F.')
tunnelServer_DialoutOptions_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("tunnelServer-DialoutOptions-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_Enabled.setDescription('Enables/Disables L2TP Dialout from this tunnel-server.')
tunnelServer_DialoutOptions_DialNumberLookup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("tunnelServer-DialoutOptions-DialNumberLookup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DialNumberLookup.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DialNumberLookup.setDescription('If enabled, uses the dial number passed by the LNS to lookup a connection profile.')
tunnelServer_DialoutOptions_LookupPrefix = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 18), DisplayString()).setLabel("tunnelServer-DialoutOptions-LookupPrefix").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_LookupPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_LookupPrefix.setDescription('A short text string prepended to the username portion of a RADIUS L2TP dial number lookup request. It is used to distinguish between DNIS and CLID authentication requests and L2TP lookup request.')
tunnelServer_DialoutOptions_DialNumberPrefix = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 19), DisplayString()).setLabel("tunnelServer-DialoutOptions-DialNumberPrefix").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DialNumberPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DialNumberPrefix.setDescription('A number to be prepended to the dialout number when placing the call. It can be used to provide locally required prefixes such as trunk numbers.')
tunnelServer_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("tunnelServer-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_Action_o.setDescription('')
mibtunnelServer_DialoutOptions_DefaultCallMappingTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 91, 2), ).setLabel("mibtunnelServer-DialoutOptions-DefaultCallMappingTable")
if mibBuilder.loadTexts: mibtunnelServer_DialoutOptions_DefaultCallMappingTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibtunnelServer_DialoutOptions_DefaultCallMappingTable.setDescription('A list of mibtunnelServer__dialout_options__default_call_mapping profile entries.')
mibtunnelServer_DialoutOptions_DefaultCallMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1), ).setLabel("mibtunnelServer-DialoutOptions-DefaultCallMappingEntry").setIndexNames((0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-DialoutOptions-DefaultCallMapping-ServerEndpoint"), (0, "ASCEND-MIBL2TUNNEL-MIB", "tunnelServer-DialoutOptions-DefaultCallMapping-Index-o"))
if mibBuilder.loadTexts: mibtunnelServer_DialoutOptions_DefaultCallMappingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibtunnelServer_DialoutOptions_DefaultCallMappingEntry.setDescription('A mibtunnelServer__dialout_options__default_call_mapping entry containing objects that maps to the parameters of mibtunnelServer__dialout_options__default_call_mapping profile.')
tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 1), DisplayString()).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-ServerEndpoint").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint.setDescription('')
tunnelServer_DialoutOptions_DefaultCallMapping_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 2), Integer32()).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_Index_o.setDescription('')
tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-ValidEntry").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry.setDescription('When FALSE, this entry should be skipped when mapping calls.')
tunnelServer_DialoutOptions_DefaultCallMapping_BearerType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 2, 3))).clone(namedValues=NamedValues(("any", 4), ("digital", 2), ("analog", 3)))).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-BearerType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_BearerType.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_BearerType.setDescription('The bearer type used for the outgoing call.')
tunnelServer_DialoutOptions_DefaultCallMapping_FramingType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 2, 3))).clone(namedValues=NamedValues(("any", 4), ("sync", 2), ("async", 3)))).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-FramingType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_FramingType.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_FramingType.setDescription('The framing type used for the outgoing call.')
tunnelServer_DialoutOptions_DefaultCallMapping_DataService = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 91, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 255, 263))).clone(namedValues=NamedValues(("voice", 1), ("n-56kRestricted", 2), ("n-64kClear", 3), ("n-64kRestricted", 4), ("n-56kClear", 5), ("n-384kRestricted", 6), ("n-384kClear", 7), ("n-1536kClear", 8), ("n-1536kRestricted", 9), ("n-128kClear", 10), ("n-192kClear", 11), ("n-256kClear", 12), ("n-320kClear", 13), ("dws384Clear", 14), ("n-448Clear", 15), ("n-512Clear", 16), ("n-576Clear", 17), ("n-640Clear", 18), ("n-704Clear", 19), ("n-768Clear", 20), ("n-832Clear", 21), ("n-896Clear", 22), ("n-960Clear", 23), ("n-1024Clear", 24), ("n-1088Clear", 25), ("n-1152Clear", 26), ("n-1216Clear", 27), ("n-1280Clear", 28), ("n-1344Clear", 29), ("n-1408Clear", 30), ("n-1472Clear", 31), ("n-1600Clear", 32), ("n-1664Clear", 33), ("n-1728Clear", 34), ("n-1792Clear", 35), ("n-1856Clear", 36), ("n-1920Clear", 37), ("x30RestrictedBearer", 39), ("v110ClearBearer", 40), ("n-64kX30Restricted", 41), ("n-56kV110Clear", 42), ("modem", 43), ("atmodem", 44), ("n-2456kV110", 46), ("n-4856kV110", 47), ("n-9656kV110", 48), ("n-19256kV110", 49), ("n-38456kV110", 50), ("n-2456krV110", 51), ("n-4856krV110", 52), ("n-9656krV110", 53), ("n-19256krV110", 54), ("n-38456krV110", 55), ("n-2464kV110", 56), ("n-4864kV110", 57), ("n-9664kV110", 58), ("n-19264kV110", 59), ("n-38464kV110", 60), ("n-2464krV110", 61), ("n-4864krV110", 62), ("n-9664krV110", 63), ("n-19264krV110", 64), ("n-38464krV110", 65), ("v32", 66), ("phs64k", 67), ("voiceOverIp", 68), ("atmSvc", 70), ("frameRelaySvc", 71), ("vpnTunnel", 72), ("wormarq", 73), ("n-14456kV110", 74), ("n-28856kV110", 75), ("n-14456krV110", 76), ("n-28856krV110", 77), ("n-14464kV110", 78), ("n-28864kV110", 79), ("n-14464krV110", 80), ("n-28864krV110", 81), ("modem31khzAudio", 82), ("x25Svc", 83), ("n-144kClear", 255), ("iptoip", 263)))).setLabel("tunnelServer-DialoutOptions-DefaultCallMapping-DataService").setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_DataService.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelServer_DialoutOptions_DefaultCallMapping_DataService.setDescription('The type of data service used for outgoing call for this bearer and framing type combination.')
mibl2TunnelGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 90, 1), )
if mibBuilder.loadTexts: mibl2TunnelGlobalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibl2TunnelGlobalTable.setDescription('A list of mibl2TunnelGlobal profile entries.')
mibl2TunnelGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1), ).setIndexNames((0, "ASCEND-MIBL2TUNNEL-MIB", "l2TunnelGlobal-Index-o"))
if mibBuilder.loadTexts: mibl2TunnelGlobalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibl2TunnelGlobalEntry.setDescription('A mibl2TunnelGlobal entry containing objects that maps to the parameters of mibl2TunnelGlobal profile.')
l2TunnelGlobal_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 1), Integer32()).setLabel("l2TunnelGlobal-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: l2TunnelGlobal_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_Index_o.setDescription('')
l2TunnelGlobal_PptpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-PptpEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_PptpEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_PptpEnabled.setDescription('Enables or disables support for the Point to Point Tunneling Protocol (PPTP).')
l2TunnelGlobal_ServerProfileRequired = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-ServerProfileRequired").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_ServerProfileRequired.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_ServerProfileRequired.setDescription("When set to 'YES', it requires that an enabled TUNNEL-SERVER profile exists before a tunnel is created. When set to 'NO', if a matching profile can't be found, the server is assumed enabled and the tunnel can be created.")
l2TunnelGlobal_L2tpMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("lac", 2), ("lns", 3), ("lacAndLns", 4)))).setLabel("l2TunnelGlobal-L2tpMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpMode.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpMode.setDescription('Layer 2 Tunneling Protocol operating mode.')
l2TunnelGlobal_L2tpAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpAuthEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpAuthEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpAuthEnabled.setDescription('Enables or disables L2TP tunnel authentication.')
l2TunnelGlobal_L2tpRxWindow = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 6), Integer32()).setLabel("l2TunnelGlobal-L2tpRxWindow").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpRxWindow.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpRxWindow.setDescription('This value is the advertised L2TP receive window size for the data channel. A value of zero indicates that this box will ask for no flow control for inbound L2TP payloads.')
l2TunnelGlobal_MaxLnsClients = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 7), Integer32()).setLabel("l2TunnelGlobal-MaxLnsClients").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_MaxLnsClients.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_MaxLnsClients.setDescription('The maximum number of clients that this box is allowed to support in LNS mode.')
l2TunnelGlobal_L2tpSystemName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 8), DisplayString()).setLabel("l2TunnelGlobal-L2tpSystemName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpSystemName.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpSystemName.setDescription('Sent to the remote tunnel endpoint during L2TP session establishment. An empty string indicates that the actual system name plus domain name will be used.')
l2TunnelGlobal_L2tpConfig_RetryTimerMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linear", 1), ("exponential", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-RetryTimerMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_RetryTimerMode.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_RetryTimerMode.setDescription('The mode in which the L2TP Control Channel Transport Layer retry timer operates. The default is Linear.')
l2TunnelGlobal_L2tpConfig_FirstRetryTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 9), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-FirstRetryTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_FirstRetryTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_FirstRetryTimer.setDescription('The first interval before the L2TP Control Channel Transport Layer retransmits a control packet, in milliseconds. Subsequent retransmissions will increase the interval.')
l2TunnelGlobal_L2tpConfig_MaxRetryTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 34), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-MaxRetryTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_MaxRetryTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_MaxRetryTimer.setDescription('The maximum timeout interval used by the L2TP Control Channel Transport Layer before retransmitting a packet, in milliseconds. 0 indicates no limit.')
l2TunnelGlobal_L2tpConfig_RetryCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 10), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-RetryCount").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_RetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_RetryCount.setDescription('The maximum number of times the L2TP Control Channel Transport Layer will retransmit a control packet.')
l2TunnelGlobal_L2tpConfig_HelloTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 11), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-HelloTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_HelloTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_HelloTimer.setDescription('The number of seconds that an L2TP Control Channel will be idle before sending a HELLO packet. If set to 0, HELLO packets will not be sent.')
l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 12), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-ControlConnectEstablishTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer.setDescription('The timeout interval for L2TP to establish a control connection session with its peer, in seconds.')
l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 13), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-LacIncomingCallTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer.setDescription('The timeout interval for the LAC to setup an incoming call with the LNS, in seconds.')
l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 14), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-LnsIncomingCallTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer.setDescription('The timeout interval for the LNS to setup an incoming call with the LAC, in seconds.')
l2TunnelGlobal_L2tpConfig_BaseUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 15), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-BaseUdpPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_BaseUdpPort.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_BaseUdpPort.setDescription('This value defines the base L2TP udp port to use for a card. A value of zero (the default) means that a non private port will be allocated dynamically.')
l2TunnelGlobal_L2tpConfig_DataPktUdpCksum = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-DataPktUdpCksum").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DataPktUdpCksum.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DataPktUdpCksum.setDescription("If IP-GLOBAL:udp-cksum is set to TRUE, setting this field to 'no' disables the locally originated UDP checksum calculation for L2TP data packets.")
l2TunnelGlobal_L2tpConfig_DialoutAuthLns = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-DialoutAuthLns").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DialoutAuthLns.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DialoutAuthLns.setDescription('Restricts the LAC to accept dialout requests only from the LNS which has authenticated during the tunnel setup.')
l2TunnelGlobal_L2tpConfig_DialoutSendProfileName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-DialoutSendProfileName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DialoutSendProfileName.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DialoutSendProfileName.setDescription('Enables the LNS to send the Connection Profile Name VSA along with the Dialout Request.')
l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-VerifyRemoteHostName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName.setDescription('If Tunnel Authentication is enabled, also verify the remote peer HostName AVP.')
l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("decimalCallSerialNumber", 2), ("hexadecimalCallSerialNumber", 3)))).setLabel("l2TunnelGlobal-L2tpConfig-AcctTunnelConnectionEncoding").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding.setDescription('Encoding of the Acct-Tunnel-Connection radius attribute')
l2TunnelGlobal_L2tpConfig_DefaultTunnelServer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 28), DisplayString()).setLabel("l2TunnelGlobal-L2tpConfig-DefaultTunnelServer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DefaultTunnelServer.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DefaultTunnelServer.setDescription('Default tunnel server profile name. Used for dialout only.')
l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-TunnelServerPreSccrqLookup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup.setDescription('When Tunnel Authentication is enabled, this parameter controls whether a lookup is to be done for the Tunnel-Server profile before sending of the SCCRQ.')
l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-SuppressEndpointDiscriminator").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator.setDescription("When set to 'yes', in the absence of a MRRU LCP option, the LAC will suppress the Endpoint Discriminator LCP option from the LCP AVPs sent to the LNS.")
l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 36), Integer32()).setLabel("l2TunnelGlobal-L2tpConfig-MaxCallsPerTunnel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel.setDescription('This value restricts the maximum number of calls that a tunnel can have at a given instance of time. When set to 0 the limit is removed.')
l2TunnelGlobal_L2tpConfig_LnsNasPortType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("virtual", 1), ("portTypeAvp", 2)))).setLabel("l2TunnelGlobal-L2tpConfig-LnsNasPortType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LnsNasPortType.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_LnsNasPortType.setDescription('LNS NAS Port Type reporting. If Virtual, report virtual. If PortTypeAvp, report as specified by LAC.')
l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4))).clone(namedValues=NamedValues(("v120", 3), ("v110", 4)))).setLabel("l2TunnelGlobal-L2tpConfig-DigitalAsyncNasPortType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType.setDescription('If LNS Acct NPT is set to PortTypeAvp but the LAC did not supply the NAS Port Type, report digital-async calls as specified here.')
l2TunnelGlobal_L2fMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("nas", 2), ("gw", 3), ("nasAndGw", 4)))).setLabel("l2TunnelGlobal-L2fMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fMode.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fMode.setDescription('Layer Two Forwarding operating mode.')
l2TunnelGlobal_L2fSystemName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 21), DisplayString()).setLabel("l2TunnelGlobal-L2fSystemName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fSystemName.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fSystemName.setDescription('Sent to the remote tunnel endpoint during L2F tunnel establishment. An empty string indicates that the actual system name plus domain name will be used.')
l2TunnelGlobal_L2fRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 22), Integer32()).setLabel("l2TunnelGlobal-L2fRetryCount").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fRetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fRetryCount.setDescription('The number of times L2F will resend control packets. The standard value as outlined in RFC2341 is 4.')
l2TunnelGlobal_L2fRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 23), Integer32()).setLabel("l2TunnelGlobal-L2fRetryInterval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fRetryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fRetryInterval.setDescription('The interval between retries in seconds. A value of 0 (zero) means that an adaptative retry interval based on the retry number is used.')
l2TunnelGlobal_L2fTunnelSecret = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sharedTunnelSecret", 1), ("distinctTunnelSecrets", 2), ("eitherSharedOrDistinctTunnelSecret", 3)))).setLabel("l2TunnelGlobal-L2fTunnelSecret").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fTunnelSecret.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fTunnelSecret.setDescription('The authentication method used on the NAS to authenticate the home Gateway during L2F Tunnel establishment.')
l2TunnelGlobal_L2fIgnoreMidSequence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("l2TunnelGlobal-L2fIgnoreMidSequence").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_L2fIgnoreMidSequence.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_L2fIgnoreMidSequence.setDescription('Determines whether a common sequence number is used for the L2F_PROTO PDUs for both the tunnel (MID=0) and the client connection.')
l2TunnelGlobal_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 90, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("l2TunnelGlobal-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2TunnelGlobal_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: l2TunnelGlobal_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBL2TUNNEL-MIB", l2TunnelGlobal_L2tpConfig_DefaultTunnelServer=l2TunnelGlobal_L2tpConfig_DefaultTunnelServer, l2TunnelGlobal_L2fMode=l2TunnelGlobal_L2fMode, tunnelServer_DialoutOptions_Enabled=tunnelServer_DialoutOptions_Enabled, l2TunnelGlobal_L2tpRxWindow=l2TunnelGlobal_L2tpRxWindow, tunnelServer_DialoutOptions_DefaultCallMapping_FramingType=tunnelServer_DialoutOptions_DefaultCallMapping_FramingType, l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer=l2TunnelGlobal_L2tpConfig_ControlConnectEstablishTimer, tunnelServer_IpsecProfile=tunnelServer_IpsecProfile, l2TunnelGlobal_L2tpConfig_MaxRetryTimer=l2TunnelGlobal_L2tpConfig_MaxRetryTimer, l2TunnelGlobal_L2tpConfig_FirstRetryTimer=l2TunnelGlobal_L2tpConfig_FirstRetryTimer, l2TunnelGlobal_L2tpConfig_DataPktUdpCksum=l2TunnelGlobal_L2tpConfig_DataPktUdpCksum, tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint=tunnelServer_DialoutOptions_DefaultCallMapping_ServerEndpoint, l2TunnelGlobal_L2tpConfig_RetryTimerMode=l2TunnelGlobal_L2tpConfig_RetryTimerMode, tunnelServer_Action_o=tunnelServer_Action_o, l2TunnelGlobal_L2tpConfig_HelloTimer=l2TunnelGlobal_L2tpConfig_HelloTimer, l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName=l2TunnelGlobal_L2tpConfig_VerifyRemoteHostName, tunnelServer_DialoutOptions_LookupPrefix=tunnelServer_DialoutOptions_LookupPrefix, mibl2TunnelGlobal=mibl2TunnelGlobal, l2TunnelGlobal_Action_o=l2TunnelGlobal_Action_o, mibl2TunnelGlobalTable=mibl2TunnelGlobalTable, tunnelServer_DialoutOptions_DefaultCallMapping_Index_o=tunnelServer_DialoutOptions_DefaultCallMapping_Index_o, tunnelServer_ValidCallTypes=tunnelServer_ValidCallTypes, l2TunnelGlobal_L2tpConfig_LnsNasPortType=l2TunnelGlobal_L2tpConfig_LnsNasPortType, l2TunnelGlobal_L2tpConfig_BaseUdpPort=l2TunnelGlobal_L2tpConfig_BaseUdpPort, l2TunnelGlobal_Index_o=l2TunnelGlobal_Index_o, mibtunnelServer_DialoutOptions_DefaultCallMappingTable=mibtunnelServer_DialoutOptions_DefaultCallMappingTable, l2TunnelGlobal_L2tpSystemName=l2TunnelGlobal_L2tpSystemName, mibtunnelServerTable=mibtunnelServerTable, tunnelServer_ServerAuthId=tunnelServer_ServerAuthId, mibtunnelServer=mibtunnelServer, l2TunnelGlobal_L2tpConfig_RetryCount=l2TunnelGlobal_L2tpConfig_RetryCount, l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer=l2TunnelGlobal_L2tpConfig_LnsIncomingCallTimer, tunnelServer_MaxClients=tunnelServer_MaxClients, l2TunnelGlobal_L2fRetryInterval=l2TunnelGlobal_L2fRetryInterval, tunnelServer_DialoutOptions_DialNumberPrefix=tunnelServer_DialoutOptions_DialNumberPrefix, tunnelServer_DialoutOptions_DefaultCallMapping_BearerType=tunnelServer_DialoutOptions_DefaultCallMapping_BearerType, l2TunnelGlobal_L2tpAuthEnabled=l2TunnelGlobal_L2tpAuthEnabled, l2TunnelGlobal_L2tpConfig_DialoutAuthLns=l2TunnelGlobal_L2tpConfig_DialoutAuthLns, tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry=tunnelServer_DialoutOptions_DefaultCallMapping_ValidEntry, l2TunnelGlobal_MaxLnsClients=l2TunnelGlobal_MaxLnsClients, tunnelServer_DialoutOptions_DefaultCallMapping_DataService=tunnelServer_DialoutOptions_DefaultCallMapping_DataService, l2TunnelGlobal_L2tpConfig_DialoutSendProfileName=l2TunnelGlobal_L2tpConfig_DialoutSendProfileName, mibtunnelServer_DialoutOptions_DefaultCallMappingEntry=mibtunnelServer_DialoutOptions_DefaultCallMappingEntry, l2TunnelGlobal_L2fSystemName=l2TunnelGlobal_L2fSystemName, l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator=l2TunnelGlobal_L2tpConfig_SuppressEndpointDiscriminator, DisplayString=DisplayString, l2TunnelGlobal_L2fRetryCount=l2TunnelGlobal_L2fRetryCount, tunnelServer_ServerEndpoint=tunnelServer_ServerEndpoint, l2TunnelGlobal_L2fIgnoreMidSequence=l2TunnelGlobal_L2fIgnoreMidSequence, tunnelServer_DialoutOptions_DialNumberLookup=tunnelServer_DialoutOptions_DialNumberLookup, l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup=l2TunnelGlobal_L2tpConfig_TunnelServerPreSccrqLookup, l2TunnelGlobal_PptpEnabled=l2TunnelGlobal_PptpEnabled, mibtunnelServerEntry=mibtunnelServerEntry, l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding=l2TunnelGlobal_L2tpConfig_AcctTunnelConnectionEncoding, l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType=l2TunnelGlobal_L2tpConfig_DigitalAsyncNasPortType, l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer=l2TunnelGlobal_L2tpConfig_LacIncomingCallTimer, l2TunnelGlobal_L2tpMode=l2TunnelGlobal_L2tpMode, l2TunnelGlobal_L2fTunnelSecret=l2TunnelGlobal_L2fTunnelSecret, tunnelServer_ClientAuthId=tunnelServer_ClientAuthId, tunnelServer_SharedSecret=tunnelServer_SharedSecret, tunnelServer_Enabled=tunnelServer_Enabled, mibl2TunnelGlobalEntry=mibl2TunnelGlobalEntry, l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel=l2TunnelGlobal_L2tpConfig_MaxCallsPerTunnel, l2TunnelGlobal_ServerProfileRequired=l2TunnelGlobal_ServerProfileRequired)
