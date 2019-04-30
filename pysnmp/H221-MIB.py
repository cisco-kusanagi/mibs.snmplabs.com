#
# PySNMP MIB module H221-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H221-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, experimental, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Unsigned32, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, Integer32, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "experimental", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Unsigned32", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "Integer32", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h221MIB = ModuleIdentity((1, 3, 6, 1, 3, 221, 2))
h221MIB.setRevisions(('1998-05-25 14:00',))
if mibBuilder.loadTexts: h221MIB.setLastUpdated('9805251400Z')
if mibBuilder.loadTexts: h221MIB.setOrganization('VTEL Corp. ')
h221Stats = MibIdentifier((1, 3, 6, 1, 3, 221, 2, 1))
h221Events = MibIdentifier((1, 3, 6, 1, 3, 221, 2, 2))
h221InFrames = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221InFrames.setStatus('current')
h221OutFrames = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221OutFrames.setStatus('current')
h221InFrameErrs = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221InFrameErrs.setStatus('current')
h221FrameAlignmentErrs = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221FrameAlignmentErrs.setStatus('current')
h221MultiFrameAlignmentErrs = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221MultiFrameAlignmentErrs.setStatus('current')
h221ErrorPerformance = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221ErrorPerformance.setStatus('current')
h221BASErrs = MibScalar((1, 3, 6, 1, 3, 221, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221BASErrs.setStatus('current')
h221TooManyErrors = NotificationType((1, 3, 6, 1, 3, 221, 2, 2, 1)).setObjects(("H221-MIB", "h221ErrorPerformance"))
if mibBuilder.loadTexts: h221TooManyErrors.setStatus('current')
h221StatsMIBConfs = MibIdentifier((1, 3, 6, 1, 3, 221, 2, 3))
h221StatsMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 221, 2, 3, 1))
h221StatsMIBCompl = MibIdentifier((1, 3, 6, 1, 3, 221, 2, 3, 2))
h221StatsGroup = ObjectGroup((1, 3, 6, 1, 3, 221, 2, 3, 1, 1)).setObjects(("H221-MIB", "h221InFrames"), ("H221-MIB", "h221OutFrames"), ("H221-MIB", "h221InFrameErrs"), ("H221-MIB", "h221FrameAlignmentErrs"), ("H221-MIB", "h221MultiFrameAlignmentErrs"), ("H221-MIB", "h221ErrorPerformance"), ("H221-MIB", "h221BASErrs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h221StatsGroup = h221StatsGroup.setStatus('current')
h221EventsGroup = NotificationGroup((1, 3, 6, 1, 3, 221, 2, 3, 1, 2)).setObjects(("H221-MIB", "h221TooManyErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h221EventsGroup = h221EventsGroup.setStatus('current')
h221StatsCompliance = ModuleCompliance((1, 3, 6, 1, 3, 221, 2, 3, 2, 1)).setObjects(("H221-MIB", "h221StatsGroup"), ("H221-MIB", "h221EventsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h221StatsCompliance = h221StatsCompliance.setStatus('current')
mibBuilder.exportSymbols("H221-MIB", h221InFrameErrs=h221InFrameErrs, h221ErrorPerformance=h221ErrorPerformance, h221StatsMIBGroups=h221StatsMIBGroups, h221TooManyErrors=h221TooManyErrors, h221MIB=h221MIB, PYSNMP_MODULE_ID=h221MIB, h221MultiFrameAlignmentErrs=h221MultiFrameAlignmentErrs, h221StatsGroup=h221StatsGroup, h221Stats=h221Stats, h221OutFrames=h221OutFrames, h221BASErrs=h221BASErrs, h221StatsMIBCompl=h221StatsMIBCompl, h221EventsGroup=h221EventsGroup, h221Events=h221Events, h221StatsCompliance=h221StatsCompliance, h221StatsMIBConfs=h221StatsMIBConfs, h221InFrames=h221InFrames, h221FrameAlignmentErrs=h221FrameAlignmentErrs)
