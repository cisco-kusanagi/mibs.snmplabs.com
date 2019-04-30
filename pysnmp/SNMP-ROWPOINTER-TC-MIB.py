#
# PySNMP MIB module SNMP-ROWPOINTER-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-ROWPOINTER-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, mib_2, Unsigned32, TimeTicks, NotificationType, IpAddress, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "mib-2", "Unsigned32", "TimeTicks", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpRowPointerTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpRowPointerTCMIB.setRevisions(('2000-12-18 00:00',))
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setLastUpdated('200012180000Z')
if mibBuilder.loadTexts: snmpRowPointerTCMIB.setOrganization('SNMP Configuration WG')
class StaticRowPointer(TextualConvention, ObjectIdentifier):
    status = 'current'

mibBuilder.exportSymbols("SNMP-ROWPOINTER-TC-MIB", snmpRowPointerTCMIB=snmpRowPointerTCMIB, StaticRowPointer=StaticRowPointer, PYSNMP_MODULE_ID=snmpRowPointerTCMIB)
