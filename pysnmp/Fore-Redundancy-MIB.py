#
# PySNMP MIB module Fore-Redundancy-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Redundancy-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hardware, atmSwitch = mibBuilder.importSymbols("Fore-Common-MIB", "hardware", "atmSwitch")
trapLogIndex, = mibBuilder.importSymbols("Fore-TrapLog-MIB", "trapLogIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, NotificationType, ModuleIdentity, Integer32, TimeTicks, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, iso, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "iso", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
asx4000RedundancyModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9))
if mibBuilder.loadTexts: asx4000RedundancyModule.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: asx4000RedundancyModule.setOrganization('FORE')
asx4000RedFabricGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1))
asx4000RedPortCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2))
asx4000RedundancyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3))
asx4000RedNetmodGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4))
class Asx4000RedundancyState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initializing", 1), ("cloning", 2), ("testing", 3), ("unprotected", 4), ("passive", 5), ("errored-detected", 6), ("armed", 7), ("requalifying", 8))

asx4000RedFabricTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1), )
if mibBuilder.loadTexts: asx4000RedFabricTable.setStatus('current')
asx4000RedFabricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1), ).setIndexNames((0, "Fore-Redundancy-MIB", "asx4000RedFabricIndex"))
if mibBuilder.loadTexts: asx4000RedFabricEntry.setStatus('current')
asx4000RedFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricIndex.setStatus('current')
asx4000RedFabricAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("unprotected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricAdminMode.setStatus('current')
asx4000RedFabricOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("unprotected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricOperState.setStatus('current')
asx4000RedFabricPendingAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("unprotected", 3), ("none", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedFabricPendingAdminMode.setStatus('current')
asx4000RedFabricCommittedState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricCommittedState.setStatus('current')
asx4000RedFabricCloningState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("done", 1), ("inprogress", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricCloningState.setStatus('deprecated')
asx4000RedFabricSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("standby", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedFabricSwitchCommand.setStatus('current')
asx4000RedFabricRedundancyState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 8), Asx4000RedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedFabricRedundancyState.setStatus('current')
asx4000RedFabricGroupCommit = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("commit", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedFabricGroupCommit.setStatus('current')
asx4000RedPortCardTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1), )
if mibBuilder.loadTexts: asx4000RedPortCardTable.setStatus('current')
asx4000RedPortCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1), ).setIndexNames((0, "Fore-Redundancy-MIB", "asx4000RedPortCardFabIndex"), (0, "Fore-Redundancy-MIB", "asx4000RedPortCardIndex"))
if mibBuilder.loadTexts: asx4000RedPortCardEntry.setStatus('current')
asx4000RedPortCardFabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedPortCardFabIndex.setStatus('current')
asx4000RedPortCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ab", 1), ("cd", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedPortCardIndex.setStatus('current')
asx4000RedPortCardCloningState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("done", 1), ("inprogress", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedPortCardCloningState.setStatus('current')
asx4000RedundancyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1), )
if mibBuilder.loadTexts: asx4000RedundancyGroupTable.setStatus('current')
asx4000RedundancyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1), ).setIndexNames((0, "Fore-Redundancy-MIB", "asx4000RedGroupName"))
if mibBuilder.loadTexts: asx4000RedundancyGroupEntry.setStatus('current')
asx4000RedGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("r12", 1), ("r34", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedGroupName.setStatus('current')
asx4000RedGroupRevertMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedGroupRevertMode.setStatus('current')
asx4000RedGroupQualifyTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 3), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedGroupQualifyTimer.setStatus('current')
asx4000RedGroupErrorThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 4), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asx4000RedGroupErrorThreshold.setStatus('current')
asx4000RedGroupErrorBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedGroupErrorBlockSize.setStatus('current')
asx4000RedNetmodTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1), )
if mibBuilder.loadTexts: asx4000RedNetmodTable.setStatus('current')
asx4000RedNetmodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1), ).setIndexNames((0, "Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"), (0, "Fore-Redundancy-MIB", "asx4000RedNetmodIndex"))
if mibBuilder.loadTexts: asx4000RedNetmodEntry.setStatus('current')
asx4000RedNetmodFabIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedNetmodFabIndex.setStatus('current')
asx4000RedNetmodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedNetmodIndex.setStatus('current')
asx4000RedNetmodRedundancyState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 3), Asx4000RedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asx4000RedNetmodRedundancyState.setStatus('current')
redundancyFabricSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2018)).setObjects(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: redundancyFabricSwitchover.setStatus('current')
redundancyFabricErrorCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 2)).setObjects(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: redundancyFabricErrorCleared.setStatus('current')
redundancyFabricErrorDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 3)).setObjects(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: redundancyFabricErrorDetected.setStatus('current')
redundancyNetmodErrorCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 4)).setObjects(("Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"), ("Fore-Redundancy-MIB", "asx4000RedNetmodIndex"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: redundancyNetmodErrorCleared.setStatus('current')
redundancyNetmodErrorDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 5)).setObjects(("Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"), ("Fore-Redundancy-MIB", "asx4000RedNetmodIndex"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: redundancyNetmodErrorDetected.setStatus('current')
mibBuilder.exportSymbols("Fore-Redundancy-MIB", asx4000RedPortCardCloningState=asx4000RedPortCardCloningState, asx4000RedFabricGroup=asx4000RedFabricGroup, asx4000RedGroupRevertMode=asx4000RedGroupRevertMode, asx4000RedundancyGroupTable=asx4000RedundancyGroupTable, redundancyNetmodErrorCleared=redundancyNetmodErrorCleared, redundancyNetmodErrorDetected=redundancyNetmodErrorDetected, asx4000RedundancyModule=asx4000RedundancyModule, PYSNMP_MODULE_ID=asx4000RedundancyModule, asx4000RedGroupErrorThreshold=asx4000RedGroupErrorThreshold, asx4000RedFabricAdminMode=asx4000RedFabricAdminMode, asx4000RedPortCardIndex=asx4000RedPortCardIndex, asx4000RedNetmodIndex=asx4000RedNetmodIndex, asx4000RedFabricRedundancyState=asx4000RedFabricRedundancyState, asx4000RedGroupQualifyTimer=asx4000RedGroupQualifyTimer, asx4000RedNetmodGroup=asx4000RedNetmodGroup, asx4000RedGroupErrorBlockSize=asx4000RedGroupErrorBlockSize, redundancyFabricErrorDetected=redundancyFabricErrorDetected, asx4000RedNetmodRedundancyState=asx4000RedNetmodRedundancyState, asx4000RedFabricGroupCommit=asx4000RedFabricGroupCommit, asx4000RedPortCardTable=asx4000RedPortCardTable, asx4000RedNetmodFabIndex=asx4000RedNetmodFabIndex, asx4000RedNetmodTable=asx4000RedNetmodTable, asx4000RedFabricTable=asx4000RedFabricTable, redundancyFabricErrorCleared=redundancyFabricErrorCleared, asx4000RedundancyGroup=asx4000RedundancyGroup, asx4000RedundancyGroupEntry=asx4000RedundancyGroupEntry, asx4000RedGroupName=asx4000RedGroupName, asx4000RedPortCardEntry=asx4000RedPortCardEntry, Asx4000RedundancyState=Asx4000RedundancyState, redundancyFabricSwitchover=redundancyFabricSwitchover, asx4000RedFabricEntry=asx4000RedFabricEntry, asx4000RedFabricPendingAdminMode=asx4000RedFabricPendingAdminMode, asx4000RedFabricCommittedState=asx4000RedFabricCommittedState, asx4000RedPortCardFabIndex=asx4000RedPortCardFabIndex, asx4000RedNetmodEntry=asx4000RedNetmodEntry, asx4000RedFabricSwitchCommand=asx4000RedFabricSwitchCommand, asx4000RedFabricIndex=asx4000RedFabricIndex, asx4000RedFabricCloningState=asx4000RedFabricCloningState, asx4000RedPortCardGroup=asx4000RedPortCardGroup, asx4000RedFabricOperState=asx4000RedFabricOperState)
