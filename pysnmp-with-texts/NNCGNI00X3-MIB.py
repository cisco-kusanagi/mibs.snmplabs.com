#
# PySNMP MIB module NNCGNI00X3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nncExtNetSynch, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtNetSynch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, IpAddress, iso, ModuleIdentity, Integer32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Integer32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter64", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class NsCandidateIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 5)

class PortIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class NsSourcePriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class NsRecoveryKind(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("manual", 1), ("automatic", 2), ("timed", 3))

class NsRecoveryTime(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1800)

class NsThreshold(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 31)

class NsOperStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("disabled", 1), ("ready", 2), ("current", 3), ("timedRecovery", 4), ("failed", 5), ("shutDown", 6), ("notReady", 7), ("autoRecovery", 8), ("cannotLock", 9), ("enabled", 10), ("illegalState", 11), ("undefinedSource", 12), ("unavailable", 13), ("acquiring", 14))

class NsAdminStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enable", 1), ("disable", 2), ("select", 3), ("deselect", 4))

nncExtNsCurrentSource = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 7, 1), NsCandidateIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNsCurrentSource.setStatus('mandatory')
nncExtNsCurrentClass = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 7, 2), NsSourcePriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNsCurrentClass.setStatus('mandatory')
nncExtNsCandidateTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 7, 3), )
if mibBuilder.loadTexts: nncExtNsCandidateTable.setStatus('mandatory')
nncExtNsCandidateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1), ).setIndexNames((0, "NNCGNI00X3-MIB", "nncExtNsCandidateIndex"))
if mibBuilder.loadTexts: nncExtNsCandidateEntry.setStatus('mandatory')
nncExtNsCandidateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 1), NsCandidateIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNsCandidateIndex.setStatus('mandatory')
nncExtNsCandidateSource = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 2), PortIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidateSource.setStatus('mandatory')
nncExtNsCandidatePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 3), NsSourcePriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidatePriority.setStatus('mandatory')
nncExtNsCandidateRecoveryKind = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2), ("timed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidateRecoveryKind.setStatus('mandatory')
nncExtNsCandidateRecoveryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 5), NsRecoveryTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidateRecoveryTime.setStatus('mandatory')
nncExtNsCandidateFailureThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 6), NsThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidateFailureThreshold.setStatus('mandatory')
nncExtNsCandidateAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("select", 3), ("deselect", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtNsCandidateAdminStatus.setStatus('mandatory')
nncExtNsCandidateOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 7, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("disabled", 1), ("ready", 2), ("current", 3), ("timedRecovery", 4), ("failed", 5), ("shutDown", 6), ("notReady", 7), ("autoRecovery", 8), ("cannotLock", 9), ("enabled", 10), ("illegalState", 11), ("undefinedSource", 12), ("unavailable", 13), ("acquiring", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtNsCandidateOperStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NNCGNI00X3-MIB", nncExtNsCandidateTable=nncExtNsCandidateTable, nncExtNsCandidateSource=nncExtNsCandidateSource, nncExtNsCandidateRecoveryKind=nncExtNsCandidateRecoveryKind, NsAdminStatus=NsAdminStatus, nncExtNsCandidateOperStatus=nncExtNsCandidateOperStatus, PortIndex=PortIndex, nncExtNsCandidateIndex=nncExtNsCandidateIndex, NsSourcePriority=NsSourcePriority, NsOperStatus=NsOperStatus, nncExtNsCandidateRecoveryTime=nncExtNsCandidateRecoveryTime, NsCandidateIndex=NsCandidateIndex, nncExtNsCandidateFailureThreshold=nncExtNsCandidateFailureThreshold, nncExtNsCurrentSource=nncExtNsCurrentSource, NsThreshold=NsThreshold, nncExtNsCurrentClass=nncExtNsCurrentClass, nncExtNsCandidateAdminStatus=nncExtNsCandidateAdminStatus, NsRecoveryTime=NsRecoveryTime, nncExtNsCandidateEntry=nncExtNsCandidateEntry, nncExtNsCandidatePriority=nncExtNsCandidatePriority, NsRecoveryKind=NsRecoveryKind)
