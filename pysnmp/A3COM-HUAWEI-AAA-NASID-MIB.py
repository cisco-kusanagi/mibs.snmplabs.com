#
# PySNMP MIB module A3COM-HUAWEI-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:48:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ModuleIdentity, Bits, Counter32, ObjectIdentity, iso, MibIdentifier, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ModuleIdentity", "Bits", "Counter32", "ObjectIdentity", "iso", "MibIdentifier", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-AAA-NASID-MIB", PYSNMP_MODULE_ID=h3cAAANasId, h3cAAANasIdTable=h3cAAANasIdTable, h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdName=h3cAAANasIdName, h3cAAANasIdObjects=h3cAAANasIdObjects, h3cAAANasId=h3cAAANasId)
