#
# PySNMP MIB module H3C-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Counter64, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, NotificationType, Gauge32, ObjectIdentity, iso, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Counter64", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cAAANasId.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cAAANasId.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cAAANasId.setDescription('This MIB contains objects to manage configuration for AAA Nas-id feature. AAA presents authentication, authorization and accouting. NAS acts as the Network Access Server. Nas-id is an identifier that contains some strings identifying the NAS.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdTable.setDescription('The AAA Nas-id table.')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "H3C-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdEntry.setDescription('The AAA Nas-id entry.')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
if mibBuilder.loadTexts: h3cAAANasIdName.setDescription('The Nas-id name.')
mibBuilder.exportSymbols("H3C-AAA-NASID-MIB", h3cAAANasIdObjects=h3cAAANasIdObjects, h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdName=h3cAAANasIdName, h3cAAANasId=h3cAAANasId, h3cAAANasIdTable=h3cAAANasIdTable, PYSNMP_MODULE_ID=h3cAAANasId)
