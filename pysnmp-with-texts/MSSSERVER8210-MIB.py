#
# PySNMP MIB module MSSSERVER8210-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSSSERVER8210-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:15:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
proElsSubSysEventMsg, = mibBuilder.importSymbols("PROTEON-MIB", "proElsSubSysEventMsg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, NotificationType, IpAddress, Bits, Counter64, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, Gauge32, Unsigned32, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
mssServer8210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2))
mss8210Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1))
mss8210PCAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2))
mss8210PCIAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3))
mss8210ResetFlag = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noreset", 1), ("reboot", 2))).clone('noreset')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8210ResetFlag.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210ResetFlag.setDescription('The flag that controls the reset process in this stand-alone. This variable shall assume a value of noreset(1) in the absence of a request for a reset from the management application. This variable shall assume a value of reboot(2) if the management application requests that this stand-alone execute a complete hardware reboot which reloads the code load from storage.')
mss8210DRAMinstalled = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210DRAMinstalled.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210DRAMinstalled.setDescription('The total amount of dynamic RAM installed on this stand-alone. The amount is in units of megabytes.')
mss8210NotifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mss8210NotifyStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210NotifyStatus.setDescription('The status of the trap reporting service in this stand-alone. This variable shall assume a value of enabled(1) if this stand-alone is permitted to send traps. This variable shall assume a value of disabled(2) if this stand-alone is prohibited from sending traps.')
mss8210TempThresholdStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210TempThresholdStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210TempThresholdStatus.setDescription('The status of the temperature in this stand-alone. This variable shall assume a value of normal(1) if the temperature is within proper operating range for this stand-alone. This variable shall assume a value of warning(2) if the temperature becomes elevated but this stand-alone can still operate. This variable shall assume a value of shutdown(3) if the temperature is beyond the operating limits of this stand-alone.')
mss8210PCAdapNumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapNumSlot.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCAdapNumSlot.setDescription('The number of PC adapter slots available for this stand-alone.')
mss8210PCAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2), )
if mibBuilder.loadTexts: mss8210PCAdapTable.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCAdapTable.setDescription('A table of PC adapters entries. The number of entries is given by the value of mss8210PCAdapNumSlot.')
mss8210PCAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1), ).setIndexNames((0, "MSSSERVER8210-MIB", "mss8210PCAdapSlotNum"))
if mibBuilder.loadTexts: mss8210PCAdapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCAdapEntry.setDescription('A PC adapter entry containing objects to describe the operational aspects of the PC adapter on this stand-alone.')
mss8210PCAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCAdapSlotNum.setDescription('The relative slot location at which the adapter is attached to this stand-alone. The slots are numbered from 1 to 2 (left to right) when facing this stand-alone. This variable serves as the index for the mss8210PCAdapTable.')
mss8210PCAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("harddrive", 2), ("modem", 3), ("notPresent", 4), ("flashcard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCAdapType.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCAdapType.setDescription('The type of PC adapter that is inserted into this slot. The variable shall assume a value of unknown(1) if the adapter in the slot is not supported by this stand-alone. The variable shall assume a value of harddrive(2) if the slot contains a PC disk drive. The variable shall assume a value of modem(3) if the slot contains a PC data/fax/voice modem. The variable shall assume a value of flashcard(5) if the slot contains a PC flash card. This variable shall assume a value of notPresent(4), when a PC card is not plugged into the corrisponding slot. ')
mss8210PCIAdapNumSlot = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapNumSlot.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapNumSlot.setDescription('The number of PCI adapter slots available for this stand-alone.')
mss8210PCIAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2), )
if mibBuilder.loadTexts: mss8210PCIAdapTable.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapTable.setDescription('A table of PCI adapters entries. The number of entries is given by the value of mss8210PCIAdapNumSlot.')
mss8210PCIAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1), ).setIndexNames((0, "MSSSERVER8210-MIB", "mss8210PCIAdapSlotNum"))
if mibBuilder.loadTexts: mss8210PCIAdapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapEntry.setDescription('A PCI adapter entry containing objects to describe the operational aspects of the PCI adapter on this stand-alone.')
mss8210PCIAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapSlotNum.setDescription('The relative slot location at which the adapter is attached to this stand-alone. Slots are numbered from 1 to 2 (top to bottom) when facing this stand-alone. This variable serves as the index for the mss8210PCIAdapTable.')
mss8210PCIAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("atm", 2), ("fddi", 3), ("notPresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapType.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapType.setDescription('The type of PCI adapter that is inserted into this slot. This variable shall assume a value of unknown(1) if the mss8210PCIAdapConfigType is not-configured(1) or if the mss8210PCIAdapConfigType is atm(2) and the mss8210PCIAdapOperStatus has a value of unknown(1), not-configured(2), not-present(3), unavailable(4), does-not_apply(5) or miss-configured(10). The variable shall assume a value of atm(2) if the mss8210PCIAdapConfigType has a value of atm(2) and the mss8210PCIAdapOperStatus has a value of enabled-pending(6), enabled(7), disabled-pending(8) or disabled(9). The variable shall assume a value of fddi(3) if the mss8210PCIAdapConfigType has a value of fddi(3) and the mss8210PCIAdapOperStatus has a value of enabled-pending(6), enabled(7), disabled-pending(8) or disabled(9). This variable shall assue a value of notPresent(4), when a PCI card is not plugged into the corrisponding slot. ')
mss8210PCIAdapConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-configured", 1), ("atm", 2), ("fddi", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapConfigType.setDescription('The router configuration type for this slot. The configuration type originates from the configuration tool used for this stand-alone. The variable shall assume a value of not-configured(1) if no configuration exist for this slot. The variable shall assume a value of atm(2) if the slot is configured for an ATM adapter. The variable shall assume a value of fddi(3) if the slot is configured for an FDDI adapter.')
mss8210PCIAdapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("unknown", 1), ("not-configured", 2), ("not-present", 3), ("unavailable", 4), ("does-not-apply", 5), ("enable-pending", 6), ("enabled", 7), ("disable-pending", 8), ("disabled", 9), ("miss-configured", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapOperStatus.setDescription('The operational status of this PCI adapter on this stand-alone. The variable shall assume a value of unknown(1) if the adapter inserted in the slot can not be recognized. The variable shall assume a value of not-configured(2) if the adapter inserted in the slot is recognized but no router configuration exists. The variable shall assume a value of not-present(3) if the adapter is not inserted in the slot but the router configuration exists. The variable shall assume a value of unavailable(4) if adapter inserted in the slot can not be used nor made ready to be used; for example, a hardware error. The variable shall assume a value of does-not-apply(5) if this adapter does not contain an operational state. The variable shall assume a value of enable-pending(6) if commands have been issued to enable the adapter but have not been completed. The variable shall assume a value of enabled(7) if commands have been successfully issued to enable the adapter. The variable shall assume a value of disable-pending(8) if commands have been issued to disable the adapter but have not been completed. The variable shall assume a value of disabled(9) if commands have been successfully issued to disable the adapter. The variable shall assume a value of miss-configured(10) if the adapter is inserted in the slot but the router configuration is of a different type.')
mss8210PCIAdapDiagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("inactive", 2), ("idle", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapDiagStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapDiagStatus.setDescription('The diagnostic status of this PCI adapter on this stand-alone. The variable shall assume a value of auto(1) if commands have been issued by the system to determine the status of the adapter; for example, at initialization. The variable shall assume a value of inactive(2) if the adapter is not currently running any diagnostics. The variable shall assume a value of idle(3) if the adapter is in the disabled operational state ready to run the diagnostics. The variable shall assume a value of active(4) if commands have been issued by the user to run the diagnostics.')
mss8210PCIAdapNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("testing", 4), ("does-not-apply", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapNetworkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapNetworkStatus.setDescription('The network status of this PCI adapter on this stand-alone. The variable shall assume a value of up(1) if the adapter is connected to the network. The variable shall assume a value of down(3) if the adapter can not verify a network connection. The variable shall assume a value of testing(4) if the adapter is running tests for the network connection. The variable shall assume a value of unknown(1) if network status can not be determined. The variable shall assume a value of does-not-apply(5) if the adapter does not contain a network state.')
mss8210PCIAdapFaultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("no-fault", 2), ("isolated", 3), ("non-isolated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mss8210PCIAdapFaultStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mss8210PCIAdapFaultStatus.setDescription('The fault status of this PCI adapter on this stand-alone. The variable shall assume a value of no-fault(2) if no fault that is associated with this adapter has been detected. The variable shall assume a value of isolated(3) if this fault that can be isolated on the adapter itself. The variable shall assume a value of non-isolated(4) if the fault can not isolated on the adapter or in the network. The variable shall assume a value of unknown(1) if the fault status has not been determined; for example, at initialization.')
mssServer8210ELSTrapV2 = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,2)).setObjects(("PROTEON-MIB", "proElsSubSysEventMsg"))
if mibBuilder.loadTexts: mssServer8210ELSTrapV2.setDescription('The trap announces that an Event Logging System (ELS) event occurred. The variable proElsSubSysEventMsg provides a textual description of the event. The variable is in one of two formats. If ELS timestamping is enabled, the format is hr:min:sec subsys_name.event_num: message_text. An example would be 09:32:56 IP.008: no rte 9.7.1.8 -> 9.7.4.3 dsc. If ELS timestamping is disabled, the format is subsys_name.event_num: message_text. An example would be IP.008: no rte 9.7.1.8 -> 9.7.4.3 dsc.')
mss8210PCAdapTypeChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,3)).setObjects(("MSSSERVER8210-MIB", "mss8210PCAdapType"))
if mibBuilder.loadTexts: mss8210PCAdapTypeChg.setDescription('The trap announces a change in the type of PC card. It shall be sent if the value of the mss8210PCAdapType changes and mss8210NotifyStatus has a value of enabled(1).')
mss8210TempThresholdChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,4)).setObjects(("MSSSERVER8210-MIB", "mss8210TempThresholdStatus"))
if mibBuilder.loadTexts: mss8210TempThresholdChg.setDescription('The trap announces a change in the temperature of the stand-alone. It shall be sent if the value of the mss8210TempThreshold changes and mss8210NotifyStatus has a value of enabled(1).')
mss8210PCIAdapStatusChg = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 118, 2) + (0,5)).setObjects(("MSSSERVER8210-MIB", "mss8210PCIAdapConfigType"), ("MSSSERVER8210-MIB", "mss8210PCIAdapOperStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapDiagStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapNetworkStatus"), ("MSSSERVER8210-MIB", "mss8210PCIAdapFaultStatus"))
if mibBuilder.loadTexts: mss8210PCIAdapStatusChg.setDescription('The trap announces a change in the status of the PCI adapter. It shall be sent if the value of either mss8210PCIAdapConfigType, mss8210PCIAdapOperStatus, mss8210PCIAdapDiagStatus, mss8210PCIAdapNetworkStatus or mss8210PCIAdapFaultStatus changes and mss8210NotifyStatus has a value of enabled(1).')
mibBuilder.exportSymbols("MSSSERVER8210-MIB", mss8210DRAMinstalled=mss8210DRAMinstalled, mss8210Prod=mss8210Prod, mss8210PCIAdapStatusChg=mss8210PCIAdapStatusChg, mss8210PCIAdapType=mss8210PCIAdapType, nwaysMSS=nwaysMSS, mss8210PCAdapTypeChg=mss8210PCAdapTypeChg, mss8210PCIAdapNetworkStatus=mss8210PCIAdapNetworkStatus, mss8210PCIAdapFaultStatus=mss8210PCIAdapFaultStatus, ibmProd=ibmProd, mss8210PCIAdapNumSlot=mss8210PCIAdapNumSlot, mss8210PCAdapType=mss8210PCAdapType, mss8210PCAdapTable=mss8210PCAdapTable, mss8210TempThresholdStatus=mss8210TempThresholdStatus, mss8210PCAdapter=mss8210PCAdapter, mssServer8210ELSTrapV2=mssServer8210ELSTrapV2, mss8210PCIAdapEntry=mss8210PCIAdapEntry, mss8210PCIAdapConfigType=mss8210PCIAdapConfigType, mss8210PCIAdapOperStatus=mss8210PCIAdapOperStatus, mss8210PCAdapEntry=mss8210PCAdapEntry, mss8210ResetFlag=mss8210ResetFlag, mss8210PCAdapSlotNum=mss8210PCAdapSlotNum, mss8210TempThresholdChg=mss8210TempThresholdChg, mss8210PCAdapNumSlot=mss8210PCAdapNumSlot, mss8210PCIAdapDiagStatus=mss8210PCIAdapDiagStatus, mssServer8210=mssServer8210, ibm=ibm, mss8210PCIAdapSlotNum=mss8210PCIAdapSlotNum, mss8210PCIAdapTable=mss8210PCIAdapTable, mss8210NotifyStatus=mss8210NotifyStatus, mss8210PCIAdapter=mss8210PCIAdapter)