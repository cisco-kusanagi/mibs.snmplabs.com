#
# PySNMP MIB module TPT-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SEGMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, Gauge32, Counter64, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, iso, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter64", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "iso", "Bits", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_segment_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19)).setLabel("tpt-segment-objs")
tpt_segment_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_segment_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_segment_objs.setOrganization('Trend Micro, Inc.')
class SegmentSflowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

segmentTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1), )
if mibBuilder.loadTexts: segmentTable.setStatus('current')
segmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1), ).setIndexNames((0, "TPT-SEGMENT-MIB", "slotIndex"), (0, "TPT-SEGMENT-MIB", "segmentIndex"))
if mibBuilder.loadTexts: segmentEntry.setStatus('current')
slotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotIndex.setStatus('current')
segmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentIndex.setStatus('current')
segmentSflowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 3), SegmentSflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentSflowStatus.setStatus('current')
sFlowDivisor = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 19, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowDivisor.setStatus('current')
mibBuilder.exportSymbols("TPT-SEGMENT-MIB", segmentSflowStatus=segmentSflowStatus, tpt_segment_objs=tpt_segment_objs, segmentTable=segmentTable, sFlowDivisor=sFlowDivisor, SegmentSflowStatus=SegmentSflowStatus, segmentIndex=segmentIndex, slotIndex=slotIndex, PYSNMP_MODULE_ID=tpt_segment_objs, segmentEntry=segmentEntry)
