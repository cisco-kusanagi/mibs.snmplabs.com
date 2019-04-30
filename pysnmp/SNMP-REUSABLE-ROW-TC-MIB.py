#
# PySNMP MIB module SNMP-REUSABLE-ROW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-REUSABLE-ROW-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, mib_2, Unsigned32, ModuleIdentity, iso, Counter64, NotificationType, TimeTicks, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "mib-2", "Unsigned32", "ModuleIdentity", "iso", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpReusableRowTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpReusableRowTCMIB.setRevisions(('2001-03-02 00:00',))
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setLastUpdated('200103020000Z')
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setOrganization('IETF Operations & Management Area')
class ReusableRow(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("reusable", 2), ("singleUse", 3))

mibBuilder.exportSymbols("SNMP-REUSABLE-ROW-TC-MIB", ReusableRow=ReusableRow, snmpReusableRowTCMIB=snmpReusableRowTCMIB, PYSNMP_MODULE_ID=snmpReusableRowTCMIB)
