#
# PySNMP MIB module H3C-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, ModuleIdentity, Gauge32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Gauge32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "Unsigned32", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "H3C-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("H3C-AAA-NASID-MIB", h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdTable=h3cAAANasIdTable, h3cAAANasId=h3cAAANasId, h3cAAANasIdObjects=h3cAAANasIdObjects, h3cAAANasIdName=h3cAAANasIdName, PYSNMP_MODULE_ID=h3cAAANasId)
