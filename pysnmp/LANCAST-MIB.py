#
# PySNMP MIB module LANCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, Counter64, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "Counter64", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lancast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2745))
lancast.setRevisions(('1999-03-03 12:00',))
if mibBuilder.loadTexts: lancast.setLastUpdated('9903031200Z')
if mibBuilder.loadTexts: lancast.setOrganization('Lancast Inc')
lancastMibModulesA = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1))
lancastTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2745, 1, 0))
mibBuilder.exportSymbols("LANCAST-MIB", PYSNMP_MODULE_ID=lancast, lancastTraps=lancastTraps, lancast=lancast, lancastMibModulesA=lancastMibModulesA)
