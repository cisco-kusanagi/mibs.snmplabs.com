#
# PySNMP MIB module Wellfleet-RREDUND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-RREDUND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Bits, MibIdentifier, ModuleIdentity, IpAddress, iso, Integer32, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "Integer32", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfRRedGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfRRedGroup")
wfRRedundGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1))
wfRRedundDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundDelete.setDescription('Create/Delete parameter')
wfRRedundDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundDisable.setDescription('Enable/Disable parameter')
wfRRedundState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("up", 1), ("waitnewpri", 2), ("rcvdprigdby", 3), ("waitprigdby", 4), ("waitsosrply", 5), ("bidding", 6), ("init", 7), ("down", 8), ("notpresent", 9))).clone('init')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundState.setDescription('State parameter')
wfRRedundGroupId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundGroupId.setDescription('Group ID parameter')
wfRRedundMemberId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundMemberId.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundMemberId.setDescription('Member ID parameter')
wfRRedundRole = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('secondary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundRole.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRole.setDescription('Role parameter')
wfRRedundRefNum = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRefNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRefNum.setDescription('Reference Number parameter, a 32 bit unsigned number.')
wfRRedundGoodIFCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundGoodIFCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundGoodIFCount.setDescription('Good Interface Count parameter, a 32 bit unsigned number.')
wfRRedundGoodRESCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundGoodRESCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundGoodRESCount.setDescription('Good Resource Count parameter, a 32 bit unsigned number.')
wfRRedundSwitch = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dontswitch", 1), ("switch", 2))).clone('dontswitch')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundSwitch.setDescription('Router software clears to indicate receive of role switch command')
wfRRedundAuto = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("manual", 1), ("auto", 2), ("oneshotauto", 3), ("failureonlyauto", 4))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundAuto.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundAuto.setDescription('Auto Role Switching parameter - Options for Auto Role Switching.')
wfRRedundGoodBidCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundGoodBidCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundGoodBidCount.setDescription('same router prior to kicking in Auto Role Switching.')
wfRRedundVersion = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 13), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundVersion.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundVersion.setDescription('Version parameter - Redundancy Protocol Version Number')
wfRRedundPriority = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundPriority.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriority.setDescription('Priority parameter - Priority level to be the Primary router')
wfRRedundHelloTimer = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundHelloTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundHelloTimer.setDescription('Secondary Keep Alives')
wfRRedundBidDuration = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(45)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundBidDuration.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBidDuration.setDescription('the Bidding Period')
wfRRedundTimeoutCounters = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundTimeoutCounters.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundTimeoutCounters.setDescription('receiving Primary Hellos before Secondaries enter the bidding process.')
wfRRedundNPrimaryCounters = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundNPrimaryCounters.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundNPrimaryCounters.setDescription('any design flaws.')
wfRRedundRoleSwitchDelayTimer = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundRoleSwitchDelayTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRoleSwitchDelayTimer.setDescription('message to adjacent routers on the non-backed-up interfaces.')
wfRRedundPriConfigFilePath = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundPriConfigFilePath.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriConfigFilePath.setDescription("Pathname of Primary's configuration file.")
wfRRedundPriMemberID = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundPriMemberID.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriMemberID.setDescription("Primary Member's Member ID")
wfRRedundPriState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("up", 1), ("waitnewpri", 2), ("rcvdprigdby", 3), ("waitprigdby", 4), ("waitsosrply", 5), ("bidding", 6), ("init", 7), ("down", 8), ("notpresent", 9))).clone('init')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundPriState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriState.setDescription("Primary Member's State")
wfRRedundPriRefNum = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundPriRefNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriRefNum.setDescription("Primary Member's Reference Number, a 32 bit unsigned value.")
wfRRedundPriGoodIFCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundPriGoodIFCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriGoodIFCount.setDescription("Primary Member's Good Interface Count, a 32 bit unsigned value.")
wfRRedundPriGoodRESCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundPriGoodRESCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundPriGoodRESCount.setDescription("Primary Member's Good Resource Count, a 32 bit unsigned value.")
wfRRedundBSecMemberID = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundBSecMemberID.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBSecMemberID.setDescription("Best Secondary Member's Member ID")
wfRRedundBSecState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("up", 1), ("waitnewpri", 2), ("rcvdprigdby", 3), ("waitprigdby", 4), ("waitsosrply", 5), ("bidding", 6), ("init", 7), ("down", 8), ("notpresent", 9))).clone('init')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundBSecState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBSecState.setDescription("Best Secondary Member's State")
wfRRedundBSecRefNum = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundBSecRefNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBSecRefNum.setDescription("Best Secondary Member's Reference Number, a 32 bit unsigned value.")
wfRRedundBSecGoodIFCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundBSecGoodIFCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBSecGoodIFCount.setDescription("Best Secondary Member's Good Interface Count, a 32 bit unsigned value.")
wfRRedundBSecGoodRESCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundBSecGoodRESCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundBSecGoodRESCount.setDescription("Best Secondary Member's Good Resource Count, a 32 bit unsigned value.")
wfRRedundWarmBoot = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundWarmBoot.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundWarmBoot.setDescription('Flag to indiacte mode of role switch. enabled is Warm-reboot vs. disabled is hot-non-reboot')
wfRRedundSlot = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundSlot.setDescription("The rredund gate's local Slot ID")
wfRRedundSlotMask = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 33), Gauge32().clone(4294705152)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundSlotMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundSlotMask.setDescription('Slot mask for which slots RREDUND is eligible to run on. The MSBit represents slot 1, the next most significant bit represents slot 2, and so on... Slots can be 1-14. Default is all slots on a BCN.')
wfRRedundAtmDeathTimer = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundAtmDeathTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundAtmDeathTimer.setDescription('Time (in milliseconds) we want to wait for the ATM driver gate to come back up, before we role-switch.')
wfRRedundCctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2), )
if mibBuilder.loadTexts: wfRRedundCctTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctTable.setDescription('This tabulates the circuit specific Router Redundancy parameters.')
wfRRedundCctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1), ).setIndexNames((0, "Wellfleet-RREDUND-MIB", "wfRRedundCctCct"))
if mibBuilder.loadTexts: wfRRedundCctEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctEntry.setDescription('Entry summary.')
wfRRedundCctDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctDelete.setDescription('Create/Delete parameter')
wfRRedundCctDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctDisable.setDescription('Enable/Disable parameter')
wfRRedundCctCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundCctCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctCct.setDescription('Circuit Number, used as Instance ID.')
wfRRedundCctPrimaryMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctPrimaryMACAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctPrimaryMACAddr.setDescription('This attribute is used for Site Manager Router Redundancy Configuration.')
wfRRedundCctMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("circuit", 1), ("link", 2))).clone('circuit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctMonitor.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctMonitor.setDescription('To indicate what element of the interface is being monitored for role switching, the circuit or the link.')
wfRRedundCctRSwitchOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctRSwitchOnFailure.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctRSwitchOnFailure.setDescription('For select triggering of role switching when interface fails ona per CCT basis.')
wfRRedundCctSendPduDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundCctSendPduDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctSendPduDisable.setDescription('For enabling/disabling sending of Router Redundancy PDU per CCT basis.')
wfRRedundCctStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundCctStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctStatus.setDescription('Status of the interface from Router Redundancy prospective.')
wfRRedundCctSONMPXmtCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundCctSONMPXmtCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctSONMPXmtCount.setDescription('Used for counting SONMP PDU transmitted on this circuit.')
wfRRedundCctSONMPRcvCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundCctSONMPRcvCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctSONMPRcvCount.setDescription('Used for counting good SONMP PDU received on this circuit.')
wfRRedundCctSONMPRcvErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundCctSONMPRcvErrorCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundCctSONMPRcvErrorCount.setDescription('Used for counting bad SONMP PDU received on this circuit.')
wfRRedundResourceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3), )
if mibBuilder.loadTexts: wfRRedundResourceTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceTable.setDescription('for Router Redundancy.')
wfRRedundResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1), ).setIndexNames((0, "Wellfleet-RREDUND-MIB", "wfRRedundResourceCircuitNumber"), (0, "Wellfleet-RREDUND-MIB", "wfRRedundResourceNetAddr"))
if mibBuilder.loadTexts: wfRRedundResourceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceEntry.setDescription('Entry summary.')
wfRRedundResourceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourceDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceDelete.setDescription('Create/Delete parameter')
wfRRedundResourceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourceDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceDisable.setDescription('Enable/Disable parameter')
wfRRedundResourceCircuitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundResourceCircuitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceCircuitNumber.setDescription('Circuit owner of this interface.')
wfRRedundResourceNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundResourceNetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceNetAddr.setDescription("Resource's Network Address, i.e. IP Address.")
wfRRedundResourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reachable", 1), ("unreachable", 2), ("unknown", 3))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundResourceStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceStatus.setDescription('Resource Status.')
wfRRedundResourceStatusUpdateDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourceStatusUpdateDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourceStatusUpdateDisable.setDescription('Resource Status Update Enable.')
wfRRedundResourcePingIntervalTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86399)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourcePingIntervalTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourcePingIntervalTimer.setDescription('Frequency timer for Pings in sec')
wfRRedundResourcePingRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourcePingRetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourcePingRetryCount.setDescription('Number of missed Pings before Resouce is unreachable')
wfRRedundResourcePingTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundResourcePingTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundResourcePingTimeOut.setDescription('Ping TimeOut in sec (wait this long before increment retry)')
wfRRedundRemoteMemberTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4), )
if mibBuilder.loadTexts: wfRRedundRemoteMemberTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberTable.setDescription('This tabulates the remote members for Router Redundancy.')
wfRRedundRemoteMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1), ).setIndexNames((0, "Wellfleet-RREDUND-MIB", "wfRRedundRemoteMemberGroupId"), (0, "Wellfleet-RREDUND-MIB", "wfRRedundRemoteMemberId"))
if mibBuilder.loadTexts: wfRRedundRemoteMemberEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberEntry.setDescription('Entry summary.')
wfRRedundRemoteMemberDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRRedundRemoteMemberDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberDelete.setDescription('Create/Delete parameter')
wfRRedundRemoteMemberGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberGroupId.setDescription('Group Member ID parameter')
wfRRedundRemoteMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberId.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberId.setDescription('Member ID parameter')
wfRRedundRemoteMemberNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberNetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberNetAddr.setDescription('Member Net Address')
wfRRedundRemoteMemberRole = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('secondary')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberRole.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberRole.setDescription('Role parameter')
wfRRedundRemoteMemberState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("up", 1), ("waitnewpri", 2), ("rcvdprigdby", 3), ("waitprigdby", 4), ("waitsosrply", 5), ("bidding", 6), ("init", 7), ("down", 8), ("notpresent", 9))).clone('init')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberState.setDescription('State parameter')
wfRRedundRemoteMemberRefNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberRefNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberRefNum.setDescription('Reference Number parameter, a 32 bit unsigned value.')
wfRRedundRemoteMemberPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberPriority.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberPriority.setDescription('Priority parameter - Priority level to be the Primary router')
wfRRedundRemoteMemberGoodIfCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberGoodIfCnt.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberGoodIfCnt.setDescription('Good interfaces count, a 32 bit unsigned value.')
wfRRedundRemoteMemberGoodResCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberGoodResCnt.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberGoodResCnt.setDescription('Good resources count, a 32 bit unsigned value.')
wfRRedundRemoteMemberIfCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberIfCnt.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberIfCnt.setDescription('Interface count')
wfRRedundRemoteMemberLocalIfReachCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRRedundRemoteMemberLocalIfReachCnt.setStatus('mandatory')
if mibBuilder.loadTexts: wfRRedundRemoteMemberLocalIfReachCnt.setDescription('Local Interface reachable count')
mibBuilder.exportSymbols("Wellfleet-RREDUND-MIB", wfRRedundPriority=wfRRedundPriority, wfRRedundCctMonitor=wfRRedundCctMonitor, wfRRedundCctSONMPXmtCount=wfRRedundCctSONMPXmtCount, wfRRedundRole=wfRRedundRole, wfRRedundCctSONMPRcvCount=wfRRedundCctSONMPRcvCount, wfRRedundCctDelete=wfRRedundCctDelete, wfRRedundCctRSwitchOnFailure=wfRRedundCctRSwitchOnFailure, wfRRedundRemoteMemberDelete=wfRRedundRemoteMemberDelete, wfRRedundAtmDeathTimer=wfRRedundAtmDeathTimer, wfRRedundRemoteMemberGoodResCnt=wfRRedundRemoteMemberGoodResCnt, wfRRedundPriRefNum=wfRRedundPriRefNum, wfRRedundCctStatus=wfRRedundCctStatus, wfRRedundPriGoodIFCount=wfRRedundPriGoodIFCount, wfRRedundCctPrimaryMACAddr=wfRRedundCctPrimaryMACAddr, wfRRedundRemoteMemberTable=wfRRedundRemoteMemberTable, wfRRedundResourcePingIntervalTimer=wfRRedundResourcePingIntervalTimer, wfRRedundGroupId=wfRRedundGroupId, wfRRedundRemoteMemberRefNum=wfRRedundRemoteMemberRefNum, wfRRedundState=wfRRedundState, wfRRedundPriConfigFilePath=wfRRedundPriConfigFilePath, wfRRedundSlot=wfRRedundSlot, wfRRedundWarmBoot=wfRRedundWarmBoot, wfRRedundMemberId=wfRRedundMemberId, wfRRedundBSecGoodRESCount=wfRRedundBSecGoodRESCount, wfRRedundDisable=wfRRedundDisable, wfRRedundRemoteMemberId=wfRRedundRemoteMemberId, wfRRedundRemoteMemberNetAddr=wfRRedundRemoteMemberNetAddr, wfRRedundRemoteMemberIfCnt=wfRRedundRemoteMemberIfCnt, wfRRedundHelloTimer=wfRRedundHelloTimer, wfRRedundResourceEntry=wfRRedundResourceEntry, wfRRedundResourceDelete=wfRRedundResourceDelete, wfRRedundResourceNetAddr=wfRRedundResourceNetAddr, wfRRedundResourcePingRetryCount=wfRRedundResourcePingRetryCount, wfRRedundGoodRESCount=wfRRedundGoodRESCount, wfRRedundNPrimaryCounters=wfRRedundNPrimaryCounters, wfRRedundSwitch=wfRRedundSwitch, wfRRedundRemoteMemberEntry=wfRRedundRemoteMemberEntry, wfRRedundCctSendPduDisable=wfRRedundCctSendPduDisable, wfRRedundRemoteMemberRole=wfRRedundRemoteMemberRole, wfRRedundBSecGoodIFCount=wfRRedundBSecGoodIFCount, wfRRedundCctEntry=wfRRedundCctEntry, wfRRedundCctCct=wfRRedundCctCct, wfRRedundRemoteMemberPriority=wfRRedundRemoteMemberPriority, wfRRedundPriGoodRESCount=wfRRedundPriGoodRESCount, wfRRedundResourceDisable=wfRRedundResourceDisable, wfRRedundGoodIFCount=wfRRedundGoodIFCount, wfRRedundSlotMask=wfRRedundSlotMask, wfRRedundBSecRefNum=wfRRedundBSecRefNum, wfRRedundRemoteMemberGroupId=wfRRedundRemoteMemberGroupId, wfRRedundRoleSwitchDelayTimer=wfRRedundRoleSwitchDelayTimer, wfRRedundBidDuration=wfRRedundBidDuration, wfRRedundPriState=wfRRedundPriState, wfRRedundGroup=wfRRedundGroup, wfRRedundCctSONMPRcvErrorCount=wfRRedundCctSONMPRcvErrorCount, wfRRedundAuto=wfRRedundAuto, wfRRedundRemoteMemberGoodIfCnt=wfRRedundRemoteMemberGoodIfCnt, wfRRedundBSecState=wfRRedundBSecState, wfRRedundRemoteMemberState=wfRRedundRemoteMemberState, wfRRedundRefNum=wfRRedundRefNum, wfRRedundBSecMemberID=wfRRedundBSecMemberID, wfRRedundPriMemberID=wfRRedundPriMemberID, wfRRedundCctTable=wfRRedundCctTable, wfRRedundVersion=wfRRedundVersion, wfRRedundResourceStatusUpdateDisable=wfRRedundResourceStatusUpdateDisable, wfRRedundResourceStatus=wfRRedundResourceStatus, wfRRedundRemoteMemberLocalIfReachCnt=wfRRedundRemoteMemberLocalIfReachCnt, wfRRedundResourcePingTimeOut=wfRRedundResourcePingTimeOut, wfRRedundCctDisable=wfRRedundCctDisable, wfRRedundTimeoutCounters=wfRRedundTimeoutCounters, wfRRedundDelete=wfRRedundDelete, wfRRedundResourceCircuitNumber=wfRRedundResourceCircuitNumber, wfRRedundResourceTable=wfRRedundResourceTable, wfRRedundGoodBidCount=wfRRedundGoodBidCount)
