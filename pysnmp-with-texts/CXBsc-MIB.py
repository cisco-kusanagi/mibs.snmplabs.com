#
# PySNMP MIB module CXBsc-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXBsc-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
cxBsc, SapIndex, Alias = mibBuilder.importSymbols("CXProduct-SMI", "cxBsc", "SapIndex", "Alias")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Bits, iso, Gauge32, Integer32, Unsigned32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Bits", "iso", "Gauge32", "Integer32", "Unsigned32", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class BscCuIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

class BscDevIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 127)

class BscRowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("invalid", 1), ("valid", 2))

class BscAckMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("endToEnd", 1), ("local", 2))

class BscOperationalMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("offline", 1), ("online", 2))

class BscBlockSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("block128", 1), ("block256", 2), ("block512", 3), ("block1k", 4), ("block2k", 5), ("block3000", 6), ("block5k", 7))

class BscStatusSense(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notSet", 1), ("isSet", 2))

bscSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10), )
if mibBuilder.loadTexts: bscSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapTable.setDescription('A table containing configuration information about all the service access point. ')
bscSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1), ).setIndexNames((0, "CXBsc-MIB", "bscSapNumber"))
if mibBuilder.loadTexts: bscSapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapEntry.setDescription('The parameters for a particular service access point.')
bscSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapNumber.setDescription('Identifies the service access point by a numerical value. This value is used as a index in the saps table. Values are unique per service access point.')
bscSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 2), BscRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapRowStatus.setDescription("Indicates whether the particular service access point is configured within the MIB. Service access point entries (rows) may be created by setting this object value to 'valid', or deleted by changing this object value to 'invalid'. Whether or not the row actually disappears is left to the implementation so this object may actually read as 'invalid' for some arbitrary length of time.")
bscSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2))).clone('lower')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapType.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapType.setDescription("Identifies the service access point by type:'lower' identifies a SAP leading to a physical BSC port. 'Upper' identifies a SAP acting as an internal inter-layer logical port.")
bscSapInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("terminalInterfaceUnit", 1), ("hostInterfaceUnit", 2))).clone('terminalInterfaceUnit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapInterfaceType.setDescription('Identifies the type of controller: either TIU or HIU.')
bscSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapAlias.setDescription('Identifies the service access point by a textual name. Names are unique per service access point.')
bscSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 6), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapCompanionAlias.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapCompanionAlias.setDescription("Identifies the `lower' service access point that will communicate with this service access point by a textual name. Names are unique per service access point. Used to bind the BSC Sap with the COP driver sap.")
bscSapSnalcRef = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscSapSnalcRef.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapSnalcRef.setDescription('Identifies which upper sap is associated to the lower sap within the BSC module. Applies only to lower BSC saps.')
bscPollIntAfterAckTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 8), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscPollIntAfterAckTimer.setStatus('mandatory')
if mibBuilder.loadTexts: bscPollIntAfterAckTimer.setDescription('This object applies only to a service access point functioning as a TIU. Determines the length of time allowed to elapse between the reception of an acknowledgment to a poll and the transmission of the next poll. Certain control units require a delay in order to successfully respond to polls. Since multiple BSC logical links may share the same SAP (i.e., multiple control units communicating on the same physical link), this timer applies globally to all logical links using this SAP. Range of values: 1 - 250 (in tenths of a second), a value of 0 disables the timer. ')
bscSapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bscSapControl.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapControl.setDescription('Control associated with the specified service access point.')
bscSapOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 30), BscOperationalMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapOperationalMode.setDescription('Identifies the service access point as being active or non-active with the new configuration.')
bscSapLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapLinkStatus.setDescription('Indicates the physical status of the sap with respect to its associated cop.')
bscSapLinkChange = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapLinkChange.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapLinkChange.setDescription('Indicates the number of times the physical link has been brought up.')
bscSapOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapOverrun.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapOverrun.setDescription("Identifies the number of block overrun's received by this sap.")
bscSapParityError = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapParityError.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapParityError.setDescription('Identifies the number of blocks received with parity errors.')
bscSapCrcError = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapCrcError.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapCrcError.setDescription('Identifies the number of blocks with CRC errors.')
bscSapBlockReject = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscSapBlockReject.setStatus('mandatory')
if mibBuilder.loadTexts: bscSapBlockReject.setDescription('Identifies the number of blocks received whose frame size is greater than that configured.')
bscCuTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11), )
if mibBuilder.loadTexts: bscCuTable.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuTable.setDescription('A table containing configuration information about all the 3270 controller units.')
bscCuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1), ).setIndexNames((0, "CXBsc-MIB", "bscCuSapNumber"), (0, "CXBsc-MIB", "bscCuNumber"))
if mibBuilder.loadTexts: bscCuEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuEntry.setDescription('The parameters for a particular controller unit.')
bscCuSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuSapNumber.setDescription('Identifies the sap associated with this controller unit. Each controller unit has an address and the address has to be unique with one sap. However, the address is not required to be unique between saps. This object is an index in the sap Table. Values are unique.')
bscCuNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 2), BscCuIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuNumber.setDescription('Identifies the address of this controller unit. The address has to be unique for a specified sap.')
bscCuRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 3), BscRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuRowStatus.setDescription("Indicates whether the particular service access point is configured within the MIB. Controller unit entries (rows) may be created by setting this object value to 'valid', or deleted by changing this object value to 'invalid'. Whether or not the row actually disappears is left to the implementation so this object may actually read as 'invalid' for some arbitrary length of time.")
bscCuHwdType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cu3271", 1), ("cu3274", 2), ("cu3275", 3), ("cu3276", 4), ("cuMES", 5))).clone('cu3275')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuHwdType.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuHwdType.setDescription('Identifies the controller unit type.')
bscCuMaxBlockLength = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 5), BscBlockSize().clone('block256')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuMaxBlockLength.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuMaxBlockLength.setDescription("Identifies the maximal length of the blocks exchanged between the host/terminal and the BSC module. The value is measured in octets and is specified by the BSC protocol. The DEFVAL value will be 'block3000' or 'block256', depending if the sap is configurated as 'hostInterfaceUnit' or 'terminalInterfaceUnit' (see the object 'bscSapInterfaceType'). ")
bscCuPollTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 250)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuPollTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuPollTimeout.setDescription('Identifies the number of seconds a station waits for an answer. The value is measured in tenth of seconds.')
bscCuDelayTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 250)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuDelayTimer.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuDelayTimer.setDescription('Identifies the number of seconds the emulated station may delay the sending of a block. Timer is in tenth of seconds.')
bscCuRetryCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuRetryCounter.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuRetryCounter.setDescription('Identifies the number of retries are executed, before a command fails. It is used by the host/terminal and the BSC layer.')
bscCuETBAck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 9), BscAckMode().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuETBAck.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuETBAck.setDescription("Identifies if the acknowledgement is local or end to end for ETBs. The ETB is a trailer block delimitator.. The 'endToEnd' means each block is acknowledged to the sender after receiving a confirmation from the remote BSC. The 'local' means the block is acknowledged locally. The block initiator is notified the block was received by the peer BSC layer.")
bscCuETXAck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 10), BscAckMode().clone('endToEnd')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscCuETXAck.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuETXAck.setDescription("Identifies if the acknowledgement is local or end to end for ETXs. The ETX is a trailer command delimitator.. The 'endToEnd' means the command is acknowledged to the sender after receiving a confirmation from the remote BSC. The 'local' means the command is acknowledged locally. The command initiator is notified the command was completed by the BSC layer. It doesn't garranty the command was completed by the remote BSC.")
bscCuControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bscCuControl.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuControl.setDescription('Control associated with the specified service access point.')
bscCuOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 30), BscOperationalMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuOperationalMode.setDescription('Identifies the service access point as being active or non-active with the new configuration.')
bscCuConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nonExistantX25Connection", 1), ("snalcConnectionRequested", 2), ("snalcConnectionConfirmationSent", 3), ("x25ConnectionEstablished", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuConnectionStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuConnectionStatus.setDescription('Indicates the X25 connection status of this link. ')
bscCuConnectRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuConnectRequest.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuConnectRequest.setDescription('Number of connection requests coming from the upper SNALC layer.')
bscCuDisconnectRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuDisconnectRequest.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuDisconnectRequest.setDescription('Number of disconnection requests coming from the upper SNALC layer.')
bscCuDisconnectIndication = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuDisconnectIndication.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuDisconnectIndication.setDescription('Number of disconnections sent to the upper SNALC layer. ')
bscCuEndToEndConnectCnf = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuEndToEndConnectCnf.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuEndToEndConnectCnf.setDescription('Number of end-to-end connections seen by the controller. Message sent by the Snalc. ')
bscCuSnalcRxRnr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuSnalcRxRnr.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuSnalcRxRnr.setDescription("Number of RNR 's received from the SNALC module due to X.25 or LLC2 flow control.")
bscCuSnalcRxRr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscCuSnalcRxRr.setStatus('mandatory')
if mibBuilder.loadTexts: bscCuSnalcRxRr.setDescription("Number of RR 's received from the SNALC module due to X.25 or LLC2 flow control.")
bscDevTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12), )
if mibBuilder.loadTexts: bscDevTable.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTable.setDescription('A table containing configuration information about all the devices controlled by this module.')
bscDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1), ).setIndexNames((0, "CXBsc-MIB", "bscDevSapNumber"), (0, "CXBsc-MIB", "bscDevCuNumber"), (0, "CXBsc-MIB", "bscDevNumber"))
if mibBuilder.loadTexts: bscDevEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevEntry.setDescription('The parameters for a particular controller unit.')
bscDevSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSapNumber.setDescription('Identifies the sap to which this device is attached. ')
bscDevCuNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 2), BscCuIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCuNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCuNumber.setDescription('Identifies the address of the controller unit to which this device is attached. ')
bscDevNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 3), BscDevIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevNumber.setDescription('Identifies the address of this device. The address has to be unique for a specified for a controller unit.')
bscDevRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 4), BscRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscDevRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRowStatus.setDescription("Indicates whether the particular service access point is configured within the MIB. Controller unit entries (rows) may be created by setting this object value to 'valid', or deleted by changing this object value to 'invalid'. Whether or not the row actually disappears is left to the implementation so this object may actually read as 'invalid' for some arbitrary length of time.")
bscDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("display", 1), ("printer", 2))).clone('display')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bscDevType.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevType.setDescription('Indicates whether the device is a printer or a display.')
bscDevControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: bscDevControl.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevControl.setDescription('Control associated with the specified service access point.')
bscDevOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 30), BscOperationalMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevOperationalMode.setDescription('Identifies the device as being active or non-active with the new configuration.')
bscDevConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nonExistantLogicalConnection", 1), ("circuitRequestSent", 2), ("circuitEnableReceived", 3), ("circuitEnableSent", 4), ("dataMode", 5))).clone('nonExistantLogicalConnection')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevConnectionStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevConnectionStatus.setDescription("Indicates the current status of the device's logical connection with regard to the network. ")
bscDevState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("hiuWaitForNextPoll", 1), ("hiuWaitingForStatusSenseAcknowledgment", 2), ("hiuSendNextMessageOnAcknowledgment", 3), ("hiuSendEotOnAcknowledgment", 4), ("hiuReceiveCommandMode", 5), ("hiuReadWaitForResponse", 6), ("hiuWaitForCuReadEtx", 7), ("hiuSendNextTransparent", 8), ("hiuWaitingForRviResponse", 9), ("hiuWaitingForWackResponse", 10), ("hiuSendNextOnNak", 11), ("hiuDeviceStateReserved-1", 12), ("hiuDeviceStateReserved-2", 13), ("hiuDeviceStateReserved-3", 14), ("tiuWaitForNextPoll", 15), ("tiuSentSpecificPoll", 16), ("tiuSentSelectivePoll", 17), ("tiuStatusSenseReceived", 18), ("tiuSendNextMessageOnAcknowledgment", 19), ("tiuSendEotOnTransparentAcknowledgment", 20), ("tiuSendEotOnAcknowledgment", 21), ("tiuDataPending", 22), ("tiuReceivingCommand", 23), ("tiuParityCursorCheckDetected", 24), ("tiuReadWaitForResponse", 25), ("tiuWaitingForSnalcData", 26), ("tiuSendNextAfterNak", 27), ("tiuTerminatePolling", 28), ("tiuEndTestRequest", 29)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevState.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevState.setDescription('Indicates the state of this link. ')
bscDevSSDeviceBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 33), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSDeviceBusy.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSDeviceBusy.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSUnitSpecify = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 34), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSUnitSpecify.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSUnitSpecify.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSDeviceEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 35), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSDeviceEnd.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSDeviceEnd.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSTransmissionCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 36), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSTransmissionCheck.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSTransmissionCheck.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSCommandReject = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 37), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSCommandReject.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSCommandReject.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSInterventionRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 38), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSInterventionRequired.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSInterventionRequired.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSEquipmentCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 39), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSEquipmentCheck.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSEquipmentCheck.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSDataCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 40), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSDataCheck.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSDataCheck.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSControlCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 41), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSControlCheck.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSControlCheck.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevSSOperationCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 42), BscStatusSense().clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSSOperationCheck.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSSOperationCheck.setDescription('The current bit information found in the last status sense message received/transmitted.')
bscDevGeneralPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 60), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevGeneralPoll.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevGeneralPoll.setDescription('Number of general polls transmitted/received.')
bscDevSpecificPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 61), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevSpecificPoll.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevSpecificPoll.setDescription('Number of specific polls transmitted/received.')
bscDevDeviceSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 62), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevDeviceSelection.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevDeviceSelection.setDescription('Number of device selections transmitted/received.')
bscDevTestRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 63), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTestRequest.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTestRequest.setDescription('Number of test request messages received.')
bscDevHostWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 64), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevHostWrite.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevHostWrite.setDescription('Number of host initiated write commands.')
bscDevHostRead = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 65), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevHostRead.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevHostRead.setDescription('Number of host initiated read commands which need a direct response.')
bscDevHostControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 66), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevHostControl.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevHostControl.setDescription('Number of host initiated control commands.')
bscDevCuShortRead = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 67), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCuShortRead.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCuShortRead.setDescription('Number of controller initiated short read commands.')
bscDevTxBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 68), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTxBlocks.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTxBlocks.setDescription('Identifies the number of blocks transmited by this controller unit.')
bscDevRxBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 69), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevRxBlocks.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRxBlocks.setDescription('Identifies the number of blocks received by this controller unit.')
bscDevStatusSense = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 70), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevStatusSense.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevStatusSense.setDescription('Identifies the number of status/sense messages received by the device.')
bscDevError = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 71), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevError.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevError.setDescription('Identifies the number of blocks in errors (other than BCC) received by this controller unit.')
bscDevErrTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 72), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevErrTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevErrTimeout.setDescription('Identifies the number of timeouts for this controller unit.')
bscDevCircuitEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 73), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCircuitEnable.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCircuitEnable.setDescription('Number of device connection requests (or enable) coming from the DSP module through the upper SNALC layer.')
bscDevCircuitDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 74), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCircuitDisconnect.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCircuitDisconnect.setDescription('Number of device disconnection requests (or disable) coming from the DSP module through the upper SNALC layer.')
bscDevCircuitRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 75), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCircuitRequest.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCircuitRequest.setDescription('Number of circuit requests sent (TIU) or received (HIU) to/from the DSP module through the upper SNALC layer.')
bscDevTxCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 76), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTxCommands.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTxCommands.setDescription('Number of complete commands transmitted to the host or controller/device.')
bscDevRxCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 77), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevRxCommands.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRxCommands.setDescription('Number of complete commands received from the host or controller/device.')
bscDevCommandsQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 78), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevCommandsQueued.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevCommandsQueued.setDescription('Number of commands queued.')
bscDevBlocksQueued = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 79), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevBlocksQueued.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevBlocksQueued.setDescription('Number of blocks queued.')
bscDevTxRvi = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 80), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTxRvi.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTxRvi.setDescription("Number of transmitted RVI's to the host. (HIU).")
bscDevRxRvi = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 81), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevRxRvi.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRxRvi.setDescription("Number of received RVI's from the controller/device.")
bscDevTxTtd = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 82), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTxTtd.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTxTtd.setDescription('Number of transmitted text delays, TTD, to the controller/device.(TIU)')
bscDevRxTtd = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 83), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevRxTtd.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRxTtd.setDescription("Number of received text delay's, TTD, from the host.(HIU)")
bscDevTxWack = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 84), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevTxWack.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevTxWack.setDescription("Number of transmitted WACK's to the host.(HIU).")
bscDevRxWack = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 85), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bscDevRxWack.setStatus('mandatory')
if mibBuilder.loadTexts: bscDevRxWack.setDescription("Number of recieved WACK's from the controller/device.")
mibBuilder.exportSymbols("CXBsc-MIB", bscSapCompanionAlias=bscSapCompanionAlias, bscCuTable=bscCuTable, bscDevEntry=bscDevEntry, bscSapControl=bscSapControl, BscRowStatus=BscRowStatus, bscDevTable=bscDevTable, bscDevRxCommands=bscDevRxCommands, bscDevRxTtd=bscDevRxTtd, bscDevError=bscDevError, bscCuOperationalMode=bscCuOperationalMode, bscDevSSDeviceEnd=bscDevSSDeviceEnd, BscStatusSense=BscStatusSense, BscCuIndex=BscCuIndex, bscCuControl=bscCuControl, bscCuRowStatus=bscCuRowStatus, bscDevCircuitDisconnect=bscDevCircuitDisconnect, bscDevBlocksQueued=bscDevBlocksQueued, bscDevTxRvi=bscDevTxRvi, bscDevSSEquipmentCheck=bscDevSSEquipmentCheck, bscDevSSOperationCheck=bscDevSSOperationCheck, bscDevDeviceSelection=bscDevDeviceSelection, bscDevRxRvi=bscDevRxRvi, bscPollIntAfterAckTimer=bscPollIntAfterAckTimer, bscDevSSCommandReject=bscDevSSCommandReject, bscCuMaxBlockLength=bscCuMaxBlockLength, bscDevSSDataCheck=bscDevSSDataCheck, bscCuSnalcRxRr=bscCuSnalcRxRr, bscSapType=bscSapType, bscDevErrTimeout=bscDevErrTimeout, bscDevState=bscDevState, bscDevHostRead=bscDevHostRead, bscCuETXAck=bscCuETXAck, bscCuPollTimeout=bscCuPollTimeout, bscSapInterfaceType=bscSapInterfaceType, bscSapAlias=bscSapAlias, bscDevRxBlocks=bscDevRxBlocks, bscDevControl=bscDevControl, bscDevCircuitRequest=bscDevCircuitRequest, bscSapLinkChange=bscSapLinkChange, bscCuConnectRequest=bscCuConnectRequest, bscSapEntry=bscSapEntry, bscCuEntry=bscCuEntry, bscCuEndToEndConnectCnf=bscCuEndToEndConnectCnf, bscSapCrcError=bscSapCrcError, BscAckMode=BscAckMode, BscOperationalMode=BscOperationalMode, bscCuETBAck=bscCuETBAck, bscCuDisconnectRequest=bscCuDisconnectRequest, bscDevGeneralPoll=bscDevGeneralPoll, bscSapRowStatus=bscSapRowStatus, bscDevSSTransmissionCheck=bscDevSSTransmissionCheck, bscDevTxTtd=bscDevTxTtd, bscSapTable=bscSapTable, bscSapOperationalMode=bscSapOperationalMode, bscDevTxCommands=bscDevTxCommands, bscDevCuShortRead=bscDevCuShortRead, bscCuSapNumber=bscCuSapNumber, bscSapParityError=bscSapParityError, bscDevTestRequest=bscDevTestRequest, bscCuConnectionStatus=bscCuConnectionStatus, bscDevSapNumber=bscDevSapNumber, bscCuDelayTimer=bscCuDelayTimer, bscDevStatusSense=bscDevStatusSense, bscCuSnalcRxRnr=bscCuSnalcRxRnr, bscDevTxWack=bscDevTxWack, bscDevCuNumber=bscDevCuNumber, bscDevType=bscDevType, bscDevSSControlCheck=bscDevSSControlCheck, bscCuHwdType=bscCuHwdType, bscSapSnalcRef=bscSapSnalcRef, bscDevSSInterventionRequired=bscDevSSInterventionRequired, BscBlockSize=BscBlockSize, bscSapLinkStatus=bscSapLinkStatus, bscDevHostControl=bscDevHostControl, bscDevCircuitEnable=bscDevCircuitEnable, bscDevConnectionStatus=bscDevConnectionStatus, bscDevRowStatus=bscDevRowStatus, bscCuNumber=bscCuNumber, bscDevOperationalMode=bscDevOperationalMode, bscCuDisconnectIndication=bscCuDisconnectIndication, bscDevHostWrite=bscDevHostWrite, bscDevSSDeviceBusy=bscDevSSDeviceBusy, bscDevNumber=bscDevNumber, bscCuRetryCounter=bscCuRetryCounter, bscDevSSUnitSpecify=bscDevSSUnitSpecify, bscDevTxBlocks=bscDevTxBlocks, BscDevIndex=BscDevIndex, bscDevSpecificPoll=bscDevSpecificPoll, bscSapNumber=bscSapNumber, bscSapBlockReject=bscSapBlockReject, bscDevRxWack=bscDevRxWack, bscDevCommandsQueued=bscDevCommandsQueued, bscSapOverrun=bscSapOverrun)
