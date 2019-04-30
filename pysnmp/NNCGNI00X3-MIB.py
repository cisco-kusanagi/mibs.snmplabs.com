#
# PySNMP MIB module NNCGNI00X3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
nncExtNetSynch, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtNetSynch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, ObjectIdentity, iso, IpAddress, Gauge32, MibIdentifier, Unsigned32, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "MibIdentifier", "Unsigned32", "Counter64", "Bits", "Integer32")
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
mibBuilder.exportSymbols("NNCGNI00X3-MIB", nncExtNsCandidateIndex=nncExtNsCandidateIndex, nncExtNsCandidateTable=nncExtNsCandidateTable, nncExtNsCandidateSource=nncExtNsCandidateSource, NsSourcePriority=NsSourcePriority, NsOperStatus=NsOperStatus, NsAdminStatus=NsAdminStatus, NsRecoveryKind=NsRecoveryKind, nncExtNsCandidateOperStatus=nncExtNsCandidateOperStatus, nncExtNsCurrentClass=nncExtNsCurrentClass, NsThreshold=NsThreshold, PortIndex=PortIndex, NsRecoveryTime=NsRecoveryTime, nncExtNsCandidateRecoveryKind=nncExtNsCandidateRecoveryKind, nncExtNsCandidateAdminStatus=nncExtNsCandidateAdminStatus, nncExtNsCandidateEntry=nncExtNsCandidateEntry, nncExtNsCandidateRecoveryTime=nncExtNsCandidateRecoveryTime, NsCandidateIndex=NsCandidateIndex, nncExtNsCandidateFailureThreshold=nncExtNsCandidateFailureThreshold, nncExtNsCurrentSource=nncExtNsCurrentSource, nncExtNsCandidatePriority=nncExtNsCandidatePriority)
