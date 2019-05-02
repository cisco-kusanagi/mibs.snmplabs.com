#
# PySNMP MIB module HH3C-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, iso, Integer32, NotificationType, ModuleIdentity, Bits, Counter32, IpAddress, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "iso", "Integer32", "NotificationType", "ModuleIdentity", "Bits", "Counter32", "IpAddress", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 114))
hh3cAAANasId.setRevisions(('2011-03-09 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cAAANasId.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hh3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: hh3cAAANasId.setOrganization('Marconi Corporation PLC.')
if mibBuilder.loadTexts: hh3cAAANasId.setContactInfo('Data Networks Team 3000 Marconi Drive,Warrendale,Pennsylvania,15086. Http://www.marconi.com E-mail:support@marconi.com')
if mibBuilder.loadTexts: hh3cAAANasId.setDescription('This MIB contains objects to manage configuration for AAA Nas-id feature. AAA presents authentication, authorization and accouting. NAS acts as the Network Access Server. Nas-id is an identifier that contains some strings identifying the NAS.')
hh3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1))
hh3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1), )
if mibBuilder.loadTexts: hh3cAAANasIdTable.setStatus('current')
if mibBuilder.loadTexts: hh3cAAANasIdTable.setDescription('The AAA Nas-id table.')
hh3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1), ).setIndexNames((0, "HH3C-AAA-NASID-MIB", "hh3cAAANasIdName"))
if mibBuilder.loadTexts: hh3cAAANasIdEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cAAANasIdEntry.setDescription('The AAA Nas-id entry.')
hh3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cAAANasIdName.setStatus('current')
if mibBuilder.loadTexts: hh3cAAANasIdName.setDescription('The Nas-id name.')
mibBuilder.exportSymbols("HH3C-AAA-NASID-MIB", hh3cAAANasId=hh3cAAANasId, hh3cAAANasIdName=hh3cAAANasIdName, hh3cAAANasIdObjects=hh3cAAANasIdObjects, PYSNMP_MODULE_ID=hh3cAAANasId, hh3cAAANasIdTable=hh3cAAANasIdTable, hh3cAAANasIdEntry=hh3cAAANasIdEntry)
