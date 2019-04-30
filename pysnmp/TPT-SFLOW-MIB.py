#
# PySNMP MIB module TPT-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SFLOW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, IpAddress, ModuleIdentity, Counter32, NotificationType, Counter64, Bits, Integer32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "NotificationType", "Counter64", "Bits", "Integer32", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_sflow_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18)).setLabel("tpt-sflow-objs")
tpt_sflow_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_sflow_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_sflow_objs.setOrganization('Trend Micro, Inc.')
class SflowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("error", 2), ("not-applicable", 3))

sFlowCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1), )
if mibBuilder.loadTexts: sFlowCollectorTable.setStatus('current')
sFlowCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1), ).setIndexNames((0, "TPT-SFLOW-MIB", "collectorIndex"))
if mibBuilder.loadTexts: sFlowCollectorEntry.setStatus('current')
collectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: collectorIndex.setStatus('current')
collectorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddr.setStatus('current')
udpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpPort.setStatus('current')
collectorAddrV6 = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: collectorAddrV6.setStatus('current')
sFlowStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 18, 2), SflowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sFlowStatus.setStatus('current')
mibBuilder.exportSymbols("TPT-SFLOW-MIB", collectorAddrV6=collectorAddrV6, SflowStatus=SflowStatus, tpt_sflow_objs=tpt_sflow_objs, collectorAddr=collectorAddr, sFlowStatus=sFlowStatus, udpPort=udpPort, collectorIndex=collectorIndex, sFlowCollectorTable=sFlowCollectorTable, PYSNMP_MODULE_ID=tpt_sflow_objs, sFlowCollectorEntry=sFlowCollectorEntry)
