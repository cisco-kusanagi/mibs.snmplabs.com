#
# PySNMP MIB module HPN-ICF-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, IpAddress, Bits, TimeTicks, Unsigned32, MibIdentifier, NotificationType, Counter64, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "IpAddress", "Bits", "TimeTicks", "Unsigned32", "MibIdentifier", "NotificationType", "Counter64", "ModuleIdentity", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114))
hpnicfAAANasId.setRevisions(('2011-03-09 09:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfAAANasId.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hpnicfAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: hpnicfAAANasId.setOrganization('')
if mibBuilder.loadTexts: hpnicfAAANasId.setContactInfo('')
if mibBuilder.loadTexts: hpnicfAAANasId.setDescription('This MIB contains objects to manage configuration for AAA Nas-id feature. AAA presents authentication, authorization and accouting. NAS acts as the Network Access Server. Nas-id is an identifier that contains some strings identifying the NAS.')
hpnicfAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1))
hpnicfAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1), )
if mibBuilder.loadTexts: hpnicfAAANasIdTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfAAANasIdTable.setDescription('The AAA Nas-id table.')
hpnicfAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-AAA-NASID-MIB", "hpnicfAAANasIdName"))
if mibBuilder.loadTexts: hpnicfAAANasIdEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfAAANasIdEntry.setDescription('The AAA Nas-id entry.')
hpnicfAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAAANasIdName.setStatus('current')
if mibBuilder.loadTexts: hpnicfAAANasIdName.setDescription('The Nas-id name.')
mibBuilder.exportSymbols("HPN-ICF-AAA-NASID-MIB", hpnicfAAANasIdTable=hpnicfAAANasIdTable, hpnicfAAANasId=hpnicfAAANasId, hpnicfAAANasIdName=hpnicfAAANasIdName, hpnicfAAANasIdObjects=hpnicfAAANasIdObjects, hpnicfAAANasIdEntry=hpnicfAAANasIdEntry, PYSNMP_MODULE_ID=hpnicfAAANasId)
