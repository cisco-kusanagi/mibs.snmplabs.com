#
# PySNMP MIB module WWP-SNMP-FRAMEWORK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SNMP-FRAMEWORK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, NotificationType, Integer32, Counter32, Gauge32, MibIdentifier, iso, ObjectIdentity, ModuleIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "Gauge32", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSnmpFrameworkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 10000))
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setLastUpdated('200510130000Z')
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setOrganization('WWP')
class SnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("WWP-SNMP-FRAMEWORK-MIB", wwpSnmpFrameworkMIB=wwpSnmpFrameworkMIB, SnmpAdminString=SnmpAdminString, PYSNMP_MODULE_ID=wwpSnmpFrameworkMIB)
