#
# PySNMP MIB module HH3C-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Counter64, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "Unsigned32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 114))
hh3cAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: hh3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: hh3cAAANasId.setOrganization('Marconi Corporation PLC.')
hh3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1))
hh3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1), )
if mibBuilder.loadTexts: hh3cAAANasIdTable.setStatus('current')
hh3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1), ).setIndexNames((0, "HH3C-AAA-NASID-MIB", "hh3cAAANasIdName"))
if mibBuilder.loadTexts: hh3cAAANasIdEntry.setStatus('current')
hh3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("HH3C-AAA-NASID-MIB", hh3cAAANasIdTable=hh3cAAANasIdTable, hh3cAAANasId=hh3cAAANasId, PYSNMP_MODULE_ID=hh3cAAANasId, hh3cAAANasIdObjects=hh3cAAANasIdObjects, hh3cAAANasIdEntry=hh3cAAANasIdEntry, hh3cAAANasIdName=hh3cAAANasIdName)
