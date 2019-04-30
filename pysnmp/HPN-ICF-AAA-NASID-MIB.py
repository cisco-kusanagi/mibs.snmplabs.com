#
# PySNMP MIB module HPN-ICF-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-AAA-NASID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Integer32, Bits, NotificationType, IpAddress, ModuleIdentity, TimeTicks, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Integer32", "Bits", "NotificationType", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114))
hpnicfAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: hpnicfAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: hpnicfAAANasId.setOrganization('')
hpnicfAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1))
hpnicfAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1), )
if mibBuilder.loadTexts: hpnicfAAANasIdTable.setStatus('current')
hpnicfAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-AAA-NASID-MIB", "hpnicfAAANasIdName"))
if mibBuilder.loadTexts: hpnicfAAANasIdEntry.setStatus('current')
hpnicfAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-AAA-NASID-MIB", hpnicfAAANasId=hpnicfAAANasId, PYSNMP_MODULE_ID=hpnicfAAANasId, hpnicfAAANasIdName=hpnicfAAANasIdName, hpnicfAAANasIdTable=hpnicfAAANasIdTable, hpnicfAAANasIdEntry=hpnicfAAANasIdEntry, hpnicfAAANasIdObjects=hpnicfAAANasIdObjects)
