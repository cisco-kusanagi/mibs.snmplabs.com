#
# PySNMP MIB module BAY-STACK-EDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-EDM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ModuleIdentity, Gauge32, Unsigned32, IpAddress, iso, TimeTicks, NotificationType, Integer32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "iso", "TimeTicks", "NotificationType", "Integer32", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEdmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 36))
bayStackEdmMib.setRevisions(('2013-10-11 00:00', '2013-02-13 00:00', '2009-08-20 00:00',))
if mibBuilder.loadTexts: bayStackEdmMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackEdmMib.setOrganization('Avaya Networks')
bayStackEdmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 0))
bayStackEdmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1))
bsEdmScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1))
bsEdmHelpFilePath = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 327))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmHelpFilePath.setStatus('current')
bsEdmInactivityTimeout = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmInactivityTimeout.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-EDM-MIB", PYSNMP_MODULE_ID=bayStackEdmMib, bayStackEdmObjects=bayStackEdmObjects, bayStackEdmNotifications=bayStackEdmNotifications, bsEdmScalars=bsEdmScalars, bsEdmHelpFilePath=bsEdmHelpFilePath, bsEdmInactivityTimeout=bsEdmInactivityTimeout, bayStackEdmMib=bayStackEdmMib)
