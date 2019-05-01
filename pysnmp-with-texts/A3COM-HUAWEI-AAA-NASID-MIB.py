#
# PySNMP MIB module A3COM-HUAWEI-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:03:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Counter64, iso, Bits, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Counter64", "iso", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cAAANasId.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cAAANasId.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cAAANasId.setDescription('This MIB contains objects to manage configuration for AAA Nas-id feature. AAA presents authentication, authorization and accouting. NAS acts as the Network Access Server. Nas-id is an identifier that contains some strings identifying the NAS.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdTable.setDescription('The AAA Nas-id table.')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdEntry.setDescription('The AAA Nas-id entry.')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdName.setDescription('The Nas-id name.')
mibBuilder.exportSymbols("A3COM-HUAWEI-AAA-NASID-MIB", h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdName=h3cAAANasIdName, h3cAAANasIdObjects=h3cAAANasIdObjects, h3cAAANasId=h3cAAANasId, PYSNMP_MODULE_ID=h3cAAANasId, h3cAAANasIdTable=h3cAAANasIdTable)
