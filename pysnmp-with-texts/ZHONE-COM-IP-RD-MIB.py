#
# PySNMP MIB module ZHONE-COM-IP-RD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-RD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Unsigned32, Integer32, Counter64, Gauge32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Unsigned32", "Integer32", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneIp, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneIp", "zhoneModules")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
comIpRd = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 53))
comIpRd.setRevisions(('2000-09-12 10:02',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: comIpRd.setRevisionsDescriptions(('V01.00.00 - Initial Release',))
if mibBuilder.loadTexts: comIpRd.setLastUpdated('200009111700Z')
if mibBuilder.loadTexts: comIpRd.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: comIpRd.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: comIpRd.setDescription('IP Routing Domain MIB IP Software Minneapolis, MN')
class ZhoneRDIndex(TextualConvention, Integer32):
    description = 'Zhone Routing Domain Index. A unique identifier for routing domains.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

rd = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3))
if mibBuilder.loadTexts: rd.setStatus('current')
if mibBuilder.loadTexts: rd.setDescription('The MIB module representing Routing Domains (RD) in Zhone Technologies products. A Routing Domain is an instance of a routing table.')
rdTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1), )
if mibBuilder.loadTexts: rdTable.setStatus('current')
if mibBuilder.loadTexts: rdTable.setDescription('The Routing Domain table contains top-level information on a Routing Domain. Other tables should use the Routing Domain table index (rdIndex) rather than define their own. Rows are added by assigning rdIndex and setting rdRowStatus to createAndGo. Rows are removed by setting rdRowStatus to destroy.')
rdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1), ).setIndexNames((0, "ZHONE-COM-IP-RD-MIB", "rdIndex"))
if mibBuilder.loadTexts: rdEntry.setStatus('current')
if mibBuilder.loadTexts: rdEntry.setDescription('An entry in the Routing Domain table.')
rdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 1), ZhoneRDIndex())
if mibBuilder.loadTexts: rdIndex.setStatus('current')
if mibBuilder.loadTexts: rdIndex.setDescription('The Routing Domain (RD) table index.')
rdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 3, 1, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdRowStatus.setStatus('current')
if mibBuilder.loadTexts: rdRowStatus.setDescription('The status of a Routing Domain entry.')
mibBuilder.exportSymbols("ZHONE-COM-IP-RD-MIB", PYSNMP_MODULE_ID=comIpRd, rdRowStatus=rdRowStatus, ZhoneRDIndex=ZhoneRDIndex, rd=rd, comIpRd=comIpRd, rdEntry=rdEntry, rdTable=rdTable, rdIndex=rdIndex)
