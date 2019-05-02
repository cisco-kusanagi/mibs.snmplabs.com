#
# PySNMP MIB module LANCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, enterprises, IpAddress, NotificationType, Gauge32, MibIdentifier, Counter32, iso, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Counter32", "iso", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lancast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2745))
lancast.setRevisions(('1999-03-03 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lancast.setRevisionsDescriptions(('REV 1.0 original Draft',))
if mibBuilder.loadTexts: lancast.setLastUpdated('9903031200Z')
if mibBuilder.loadTexts: lancast.setOrganization('Lancast Inc')
if mibBuilder.loadTexts: lancast.setContactInfo('Contact: Customer Service Tel: 1-800-526-2278 ext 136 Fax: 1-603-594-2887 Web: info@lancast.com')
if mibBuilder.loadTexts: lancast.setDescription('This is the enterprise MIB definition file for all Lancast Managed products. Copyright 1999 Lancast Inc.')
lancastMibModulesA = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1))
lancastTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1, 0))
mibBuilder.exportSymbols("LANCAST-MIB", lancastTraps=lancastTraps, lancastMibModulesA=lancastMibModulesA, PYSNMP_MODULE_ID=lancast, lancast=lancast)
