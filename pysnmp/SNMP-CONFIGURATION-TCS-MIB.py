#
# PySNMP MIB module SNMP-CONFIGURATION-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-CONFIGURATION-TCS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, Bits, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, mib_2, Counter64, MibIdentifier, Integer32, Counter32, Unsigned32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "mib-2", "Counter64", "MibIdentifier", "Integer32", "Counter32", "Unsigned32", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpConfigurationTCsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpConfigurationTCsMIB.setRevisions(('2000-11-14 00:00',))
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setLastUpdated('200011140000Z')
if mibBuilder.loadTexts: snmpConfigurationTCsMIB.setOrganization('SNMP Configuration WG')
class DynamicRowPointer(TextualConvention, ObjectIdentifier):
    status = 'current'

class StaticRowPointer(TextualConvention, ObjectIdentifier):
    status = 'current'

mibBuilder.exportSymbols("SNMP-CONFIGURATION-TCS-MIB", PYSNMP_MODULE_ID=snmpConfigurationTCsMIB, snmpConfigurationTCsMIB=snmpConfigurationTCsMIB, DynamicRowPointer=DynamicRowPointer, StaticRowPointer=StaticRowPointer)
