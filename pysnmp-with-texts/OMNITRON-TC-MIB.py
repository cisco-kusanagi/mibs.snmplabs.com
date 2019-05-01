#
# PySNMP MIB module OMNITRON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OMNITRON-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, TimeTicks, Counter32, ModuleIdentity, iso, Gauge32, IpAddress, enterprises, Bits, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Gauge32", "IpAddress", "enterprises", "Bits", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ostOmnitronTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7342, 11))
ostOmnitronTcMib.setRevisions(('2015-05-13 12:00', '2015-01-21 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ostOmnitronTcMib.setRevisionsDescriptions(('Added OstIpv6Addr, OstIpAddr ', 'Initial version of v5.2 MIB. Added OstAccessibiltyType from the OMNITRON-ACL-MIB ',))
if mibBuilder.loadTexts: ostOmnitronTcMib.setLastUpdated('201505131200Z')
if mibBuilder.loadTexts: ostOmnitronTcMib.setOrganization('Omnitron Systems Technology, Inc.')
if mibBuilder.loadTexts: ostOmnitronTcMib.setContactInfo('Omnitron Systems Technology, Inc. 38 Tesla Irvine, CA 92618-4670 USA Tel: (949) 250 6510 Fax: (949) 250 6514 E-mail: info@omnitron-systems.com International: +1 949 250 6510 Technical Support and Customer Service Tel: (800) 675 8410 E-mail: support@omnitron-systems.com International: +1 949 250 6510')
if mibBuilder.loadTexts: ostOmnitronTcMib.setDescription('Omnitron TC MIB for use with v5.2 iConverter Management Modules and NetOutlook Copyright 2015 Omnitron Systems Technology, Inc. All rights reserved ')
omnitron = MibIdentifier((1, 3, 6, 1, 4, 1, 7342))
icAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 1))
class OstAccessibiltyType(TextualConvention, Integer32):
    description = 'Accessibilty type enumeration. deny(1) Access to the module is not allowed permit(2) Access to the module is allowed '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class OstClassOfService(TextualConvention, Unsigned32):
    description = 'Class of service setting. 0=discard, 1=lowest class, 4=highest class'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class OstClockFreq(TextualConvention, Unsigned32):
    description = 'Clock frequency in hundreths of MHz.'
    status = 'current'
    displayHint = 'd-2'

class OstCosL2cpDstAddr(TextualConvention, Unsigned32):
    description = 'L2CP destination address enumeration. Index | Destination Address | Name ------+---------------------+---------- 1 | 01-80-C2-00-00-00 | RSTP 2 | 01-80-C2-00-00-01 | Pause 3 | 01-80-C2-00-00-02 | LACP 4 | 01-80-C2-00-00-02 | Marker 5 | 01-80-C2-00-00-02 | Link OAM 6 | 01-80-C2-00-00-02 | 7 | 01-80-C2-00-00-03 | 802.1x 8 | 01-80-C2-00-00-04 | IEEE MAC 9 | 01-80-C2-00-00-05 | 10 | 01-80-C2-00-00-06 | 11 | 01-80-C2-00-00-07 | E-LMI 12 | 01-80-C2-00-00-08 | Pr Bridge 13 | 01-80-C2-00-00-09 | 14 | 01-80-C2-00-00-0A | 15 | 01-80-C2-00-00-0B | 16 | 01-80-C2-00-00-0C | 17 | 01-80-C2-00-00-0D | GVRP 18 | 01-80-C2-00-00-0E | LLDP 19 | 01-80-C2-00-00-0F | 20 | 01-80-C2-00-00-20 | GARP '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 20)

class OstCosNameString(TextualConvention, OctetString):
    description = 'A class of service name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstCosNameStringOrNone(TextualConvention, OctetString):
    description = 'A class of service name or an empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstCosTrustType(TextualConvention, Integer32):
    description = 'CoS trust type enumeration. Green traffic is marked with low drop precedence and yellow traffic is marked with high drop precedence. cosTrust(1) Trust frame. The frames priority determines the egress class. cosUsePri(2) Use the priority ostCosPriority for the frame. The frame will egress with ostCosPriority priority and ostCosPrirority determines the egress class. cosUseClass(3) Use the class ostCosClass for the frame. The frame will egress with the frames priority and the ostCosClass egress class. cosUsePriClass(4) Use the priority ostCosPriority and class ostCosClass for the frame. The frames will egress with ostCosPri and ostCosClass egress class. cosGreenYellow(5) Use ostCosGreenPriority and ostCosGreenClass for green traffic. Use ostCosYellowPriority and ostCosYellowClass for yellow traffic. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cosTrust", 1), ("cosUsePri", 2), ("cosUseClass", 3), ("cosUsePriClass", 4), ("cosGreenYellow", 5))

class OstEgressSchedulingProfileIndexType(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies an Egress Scheduling Profile. The valid values are 1 to X, where X is the maximum supported profile. The maximum value for X for the GM4 is 4. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstEgressQueueIndexType(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies an Egress Queue. The valid values are 1 to X, where X is the maximum supported profile. The maximum value for X for the GM4 is 4. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstElpsProtectType(TextualConvention, Integer32):
    description = 'A value that represents the ELPS protection type. The value can be one of the following: e1plus1UniNoAps(1) 1+1 unidirectional without APS communication e1plus1UniAps(2) 1+1 unidirectional switching with APS communication e1plus1BiAps(3) 1+1 bidirectional w/APS communication e1to1(4) 1:1 bidirectional w/APS communication notAvailable(5) Protect Type is unknown or not available, value returned for status read, not allowed to write '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("e1plus1UniNoAps", 1), ("e1plus1UniAps", 2), ("e1plus1BiAps", 3), ("e1to1", 4), ("notAvailable", 5))

class OstElpsRequestStates(TextualConvention, Integer32):
    description = 'A value that represents the current request/state of either the local or remote (partner) ELPS instance. The value can be one of the following: noRequest(0) No Request (NR), lowest priority doNotRevert(1) Do Not Revert (DNR) revertRequest(2) Revert request (RR) exercise(4) Exercise APS protocol (EXER) waitToRestore(5) Wait to restore (WTR) manualSwitchWorking(6) Manual swtich to working (MS-W) manualSwitch(7) Manual switch (MS) signalDegrade(9) Signal degrade (SD) signalFailWorking(11) Signal fail for working (SF) forcedSwitch(13) Forced switch (FS) signalFailProtection(14) Signal fail for protection (SF-P) lockoutProtection(15) Lock of protection (LO), highest priority notAvailable(16) Status is unknown or not available, value returned for status read, not allowed to write '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16))
    namedValues = NamedValues(("noRequest", 0), ("doNotRevert", 1), ("revertRequest", 2), ("exercise", 4), ("waitToRestore", 5), ("manualSwitchWorking", 6), ("manualSwitch", 7), ("signalDegrade", 9), ("signalFailWorking", 11), ("forcedSwitch", 13), ("signalFailProtection", 14), ("lockoutProtection", 15), ("notAvailable", 16))

class OstElpsSignalStates(TextualConvention, Integer32):
    description = 'A value that represents the requested or bridged signal for either the local or remote (partner) ELPS instance. The value can be one of the following: nullSignal(0) Null signal. This indicates the signal that the near-end requests be carried over the protection path normalSignal(1) Normal traffic signal. This indicates the signal that is bridged onto the protection path. notAvailable(2) Protect Type is unknown or not available, value returned for status read, not allowed to write '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nullSignal", 0), ("normalSignal", 1), ("notAvailable", 2))

class OstErpsLinkState(TextualConvention, Integer32):
    description = 'A value that represents the current port link state. This is a function that indicates whether the current port is linked. The value can be one of the following: na(0) Not Applicable, port state is unknown up(1) Port is linked and capable of passing traffic down(2) Port is not linked and is not capable of passing traffic '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class OstErpsPortState(TextualConvention, Integer32):
    description = 'A value that represents the current forwarding state of the port. The value can be one of the following: na(0) Not Applicable, port state is unknown forward(1) Port is in the forwarding state blocked(2) Port is in the blocked state '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("forward", 1), ("blocked", 2))

class OstErpsPortType(TextualConvention, Integer32):
    description = 'A value that represents the Ring Port type. The value can be one of the following: rp0(1) Ring Port 0 rp1(2) Ring Port 1 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rp0", 1), ("rp1", 2))

class OstErpsRingStates(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-1'
    description = 'A value that represents the current request/state of either the local or remote (partner) ERPS instance. The value can be one of the following: noRequest(0) No Request (NR), local, lowest priority rapsNr(1) Ring APS (R-APS) No Request (NR), remote rapsNrRb(2) Ring APS (R-APS) No Request (NR), RPL Blocked (RB), remote wtbRunning(3) Wait to Block (WTB) running, local wtbExpires(4) Wait to Block (WTB) expires, local wtrRunning(5) Wait to Restore (WTR) running, local wtrExpires(6) Wait to Restore (WTR) expires, local manualSwitch(7) Manual Switch (MS), local rapsManualSwitch(8) Ring APS (R-APS) Manual Switch (MS), remote rapsSignalFail(9) Ring APS (R-APS) Signal Fail (SF), remote localClearSignalFail(10) Local clear Signal Fail (SF), local localSignalFail(11) Local Signal Fail (SF), local rapsForcedSwitch(12) Ring APS (R-APS) Forced Switch (FS), remote forcedSwtich(13) Forced Switch (FS), local clear(14) Clear, local '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("noRequest", 0), ("rapsNr", 1), ("rapsNrRb", 2), ("wtbRunning", 3), ("wtbExpires", 4), ("wtrRunning", 5), ("wtrExpires", 6), ("manualSwitch", 7), ("rapsManualSwitch", 8), ("rapsSignalFail", 9), ("localClearSignalFail", 10), ("localSignalFail", 11), ("rapsForcedSwitch", 12), ("forcedSwtich", 13), ("clear", 14))

class OstErpsRingStatus(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-2'
    description = 'A value that represents the current ring status. This is state machine node state value for the ERPS instance. The value can be one of the following: initializing(1) State machine initialization idle(2) Idle State (A) protection(3) Protection (B) manualSwitch(4) Manual Switch (C) forcedSwitch(5) Forced Switch (D) pending(6) Pending (E) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initializing", 1), ("idle", 2), ("protection", 3), ("manualSwitch", 4), ("forcedSwitch", 5), ("pending", 6))

class OstErrorString(TextualConvention, OctetString):
    description = 'The SNMP error string for further definition of a SNMP error.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class OstEvcNameString(TextualConvention, OctetString):
    description = 'An EVC name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstEvcNameStringOrNone(TextualConvention, OctetString):
    description = 'An EVC name or an empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstFileNameString(TextualConvention, OctetString):
    description = 'A internal file name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstFingerprintString(TextualConvention, OctetString):
    description = 'The fingerprint value for SSH protocol.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class OstFloatValue(TextualConvention, OctetString):
    description = 'Floating point data type as represented in an octet string. Legal values and precision are indicated by the appropriate object. Only numbers and the decimal place are legal digit values. Example values: 1000 1500.05 1545.25 '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class OstFrameCount64(TextualConvention, Counter64):
    description = 'Frame counter value.'
    status = 'current'
    displayHint = 'd'

class OstFrameSizeList(TextualConvention, OctetString):
    description = " Denotes a list of one or more frame sizes. 1. Frame sizes have a value from 64 to 10240 bytes for the GM3, GM4, and GM4-PoE. Frame sizes have a value from 64 to 10240 bytes for the XM5. 2. Individual frame sizes are included when separated by a comma ','. 3. A range of frame sizes is included when separated by '..'. 4. A range of sizes ending in a colon and a value, i.e. start..end:value, is the frame increment size for the next iteration (min value is 4) 5. Ranges must be organized min size to max size, i.e. min..max 6. Individual sizes can be mixed in any order Example values: 64 64..1024:64 64,128,256,512,1024,1280,1518,10000 "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class OstIndexIntegerNextFree(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a new index in a table. The special value of 0 indicates that no more new entries can be created in the relevant table. When a MIB is used for configuration, an object with this SYNTAX always contains a legal value (if non-zero) for an index that is not currently used in the relevant table. The Command Generator (Network Management Application) reads this variable and uses the (non-zero) value read when creating a new row with an SNMP SET. When the SET is performed, the Command Responder (agent) MUST determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation-specific algorithm. If the value is in use, however, the SET fails. The Network Management Application MUST then re-read this variable to obtain a new usable value. An OBJECT-TYPE definition using this SYNTAX MUST specify the relevant table for which the object is providing this functionality. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class OstIpPriorityList(TextualConvention, OctetString):
    description = 'Selects IP priority values. Valid values are from 0 to 63. Format: X selects a single PCP priority value X..Y selects a range of PCP priority values, X to Y X,Y selects PCP priority values seperated by a comma Example values: 0 2..5 0,2..5 '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstIpv6Addr(TextualConvention, OctetString):
    description = 'This data type is used to model the IPv6 address. This is a binary string of up to 8 octets in network byte-order. '
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class OstIpAddr(TextualConvention, OctetString):
    description = "This data type is used to model both IPv4 and IPv6 addresses. It is a hexadecimcal octet string with separators between number groups: either '.' for IPv4 or ':' for IPv6. The IP type is derived based upon the format of the string. Valid IP addreses: '192.168.1.220' 'fe80:0000:0:0:1234:5678:abcd:efff' "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 39)

class OstMhfCreation(TextualConvention, Integer32):
    description = 'Indicates if the Management Entity can create MHFs. The valid values are: ostMHFdefault(2) MHFs can be created on this VID on any Bridge port through which this VID can pass. ostMHFexplicit(3) MHFs can be created for this VID only on Bridge ports through which this VID can pass, and only if a MEP is created at some lower MD Level. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ostMHFdefault", 1), ("ostMHFexplicit", 2))

class OstMipdMethodOfCreation(TextualConvention, Integer32):
    description = 'Indicates the method of how this Mip table entry was created The valid values are: ostExplicit(1) indicates the Mip was created explicitly through a command. ostImplicitMa(2) indicates the Mip was created implicitly through the MA command. ostImplicitMde(3) indicates the Mip was created implicitly through the CFM default Md table. ostExplicitImplicitMa(4) indicates the Mip was created both implicitly and explicitly through the MA command. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ostExplicit", 1), ("ostImplicitMa", 2), ("ostImplicitMde", 3), ("ostExplicitImplicitMa", 4))

class OstModeType(TextualConvention, Integer32):
    description = 'The module Mode Type as AP, SP or neither. normal(1) Not specifically AP or SP ap(2) Access Provider sp(3) Service Provider '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("ap", 2), ("sp", 3))

class OstModuleSingleIndex(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies the chassis and slot in which the module is located. Base 10 Format: CCSS where CC is the chassis index, 1 to 99 SS is the slot index, 1 to 99'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(101, 9999)

class OstPcpPriorityList(TextualConvention, OctetString):
    description = 'Selects PCP priority values. Valid values are from 0 to 7. Format: X selects a single PCP priority value X..Y selects a range of PCP priority values, X to Y X,Y selects PCP priority values seperated by a comma Example values: 0 2..5 0,2..5 '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstPortClockType(TextualConvention, Integer32):
    description = 'A value that indicates the TDM port recovery state/mode. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("adaptiveIdle", 1), ("adaptiveAcqu", 2), ("adaptiveTrk1", 3), ("adaptiveTrk2", 4), ("holdOver", 5), ("coax", 6), ("internal", 7), ("line", 8))

class OstPortList(TextualConvention, OctetString):
    description = "Denotes a list of one or more ports, separated by comma characters, in the form of an ASCII string, which is case insensitive. Port Description ---- ------------------ 1 Port 1 2 Port 2 3 Port 3 4 Port 4 5 Port 5 6 Port 6 7 Port 7 8 Port 8 9 Port 9 10 Port 10 11 Port 11 12 Port 12 13 Port 13 14 Port 14 15 Port 15 16 Port 16 17 Port 17 a backplane port A b backplane port B mgt1 management port 1 mgt2 management port 2 all includes all ports Example: '1,2,a,mgt1' "
    status = 'current'
    displayHint = '255a'

class OstPortNumber(TextualConvention, Unsigned32):
    description = "This object selects the port number for the specific test instance that is configured. This value is dependent upon actual product accessed. The port number for a specific port can be determined by selecting the module type and then the port that is accessed. A value of '0' indicates that no port is defined. Module Type P1 P2 P3 P4 P5 BP A BP B Mgt1 Mgt2 ----------------- --- --- --- --- --- ---- ---- ---- ---- 3-port plug-in 1 2 3 n/a n/a 4 5 6 7 3-port standalone 1 2 3 n/a n/a n/a n/a 6 7 2-port plug-in 1 2 n/a n/a n/a 3 4 5 6 2-port standalone 1 2 n/a n/a n/a n/a n/a 5 6 4-port 1 2 3 4 n/a 5 6 n/a n/a 5-port 1 2 3 4 5 n/a n/a 6 7 For the 7 port module: Port 1 - Port 7 are ports 1 - 7 are the front facing ports, port 8 is the dedicated management port, port 9 is Mgt1 and port 10 is Mgt2. For the 16 port module: Port 1 - Port 16 are the customer facing ports, port 17 is the dedicated management port, port 18 is Mgt1 and port 19 is Mgt2. Other values are undefined. "
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 99)

class OstPortSingleIndex(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies a module port, and the chassis and slot in which the module is located. Base 10 Format: CCSSPP where CC is the chassis index, 1 to 99 SS is the slot index, 1 to 99 PP is the port index, 1 to 99'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(10101, 999999)

class OstPriority(TextualConvention, Unsigned32):
    description = 'Priority setting.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class OstProbeNameString(TextualConvention, OctetString):
    description = 'An EVC name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstProfileNameString(TextualConvention, OctetString):
    description = 'A test profile name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstTestResultType(TextualConvention, Integer32):
    description = 'A value that indicates the result of a test. The value can be one of the following: pass(1) Indicates the test has passed successfully fail(2) Indicates the test has failed oversubscribe(3) Indicates the test failed due to oversubscription of a resource '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pass", 1), ("fail", 2), ("oversubscribe", 3))

class OstTestStatusType(TextualConvention, Integer32):
    description = 'A value that indicates the status of the current test instance. The value can be one of the following: testNotStarted(1) Current test instance has not started yet, not fully configured, or waiting for loop-up testInProcess(2) Current test instance is currently running testStopped(3) Current test instance has been stopped after running for a period of time testCompleted(4) Current test instance has completed testInitializing(5) Current test is the process of starting, used to restart a test in process, completed, or stopped '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("testNotStarted", 1), ("testInProcess", 2), ("testStopped", 3), ("testCompleted", 4), ("testInitializing", 5))

class OstUnsigned64(TextualConvention, Counter64):
    description = 'A non-negative 64-bit bit integer, without counter semantics, between 0 and 2^64-1 inclusive (0 to 18446744073709551615 decimal). It can have a MAX-ACCESS of read-only or read-write. SYNTAX is Counter64 for the encoding rules only. '
    status = 'current'
    displayHint = 'd'

class OstUserNameString(TextualConvention, OctetString):
    description = 'A string that is used to identify a specific user.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class OstVlanId(TextualConvention, Integer32):
    description = 'The VLAN-ID that uniquely identifies a VLAN. This is the 12-bit VLAN-ID used in the VLAN Tag header.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class OstVlanIdList(TextualConvention, OctetString):
    description = "Denotes a list of one or more VLAN IDs. VLAN IDs have a value of 0 to 4095. Individual VLAN IDs are included when separated by a comma ','. A range of VLAN IDs is included when separated by '..'. An asterisk indicates untagged data. 'rest' selects remaining VLAN IDs. 'all' selects all VLAN IDs. Example values: 100,110 100..110 100,110,200..210 100,110,200..210,500..510 "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 110)

mibBuilder.exportSymbols("OMNITRON-TC-MIB", OstElpsSignalStates=OstElpsSignalStates, OstPriority=OstPriority, ostOmnitronTcMib=ostOmnitronTcMib, OstFloatValue=OstFloatValue, OstErrorString=OstErrorString, OstProbeNameString=OstProbeNameString, OstVlanIdList=OstVlanIdList, OstElpsProtectType=OstElpsProtectType, OstClockFreq=OstClockFreq, OstIpPriorityList=OstIpPriorityList, OstPortNumber=OstPortNumber, OstAccessibiltyType=OstAccessibiltyType, OstMhfCreation=OstMhfCreation, OstIpv6Addr=OstIpv6Addr, OstFingerprintString=OstFingerprintString, OstUserNameString=OstUserNameString, icAgent=icAgent, OstFrameCount64=OstFrameCount64, OstErpsPortState=OstErpsPortState, OstEvcNameStringOrNone=OstEvcNameStringOrNone, OstCosNameStringOrNone=OstCosNameStringOrNone, OstEvcNameString=OstEvcNameString, OstIpAddr=OstIpAddr, OstEgressSchedulingProfileIndexType=OstEgressSchedulingProfileIndexType, OstProfileNameString=OstProfileNameString, OstCosTrustType=OstCosTrustType, OstTestResultType=OstTestResultType, OstPortList=OstPortList, OstTestStatusType=OstTestStatusType, OstVlanId=OstVlanId, OstClassOfService=OstClassOfService, OstCosNameString=OstCosNameString, OstPcpPriorityList=OstPcpPriorityList, omnitron=omnitron, OstFileNameString=OstFileNameString, OstEgressQueueIndexType=OstEgressQueueIndexType, OstMipdMethodOfCreation=OstMipdMethodOfCreation, OstUnsigned64=OstUnsigned64, OstCosL2cpDstAddr=OstCosL2cpDstAddr, OstErpsRingStatus=OstErpsRingStatus, OstPortClockType=OstPortClockType, OstModuleSingleIndex=OstModuleSingleIndex, OstPortSingleIndex=OstPortSingleIndex, OstIndexIntegerNextFree=OstIndexIntegerNextFree, OstErpsPortType=OstErpsPortType, OstErpsRingStates=OstErpsRingStates, PYSNMP_MODULE_ID=ostOmnitronTcMib, OstErpsLinkState=OstErpsLinkState, OstElpsRequestStates=OstElpsRequestStates, OstFrameSizeList=OstFrameSizeList, OstModeType=OstModeType)
