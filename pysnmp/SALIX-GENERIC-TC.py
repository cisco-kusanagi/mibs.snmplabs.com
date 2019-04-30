#
# PySNMP MIB module SALIX-GENERIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-GENERIC-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
salixGeneric, = mibBuilder.importSymbols("SALIX-MIB", "salixGeneric")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Gauge32, NotificationType, Integer32, Unsigned32, IpAddress, ObjectIdentity, Bits, ModuleIdentity, TimeTicks, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "ModuleIdentity", "TimeTicks", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
salixGenericTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 2))
if mibBuilder.loadTexts: salixGenericTc.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixGenericTc.setOrganization('SALIX Technologies')
class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("SALIX-GENERIC-TC", salixGenericTc=salixGenericTc, PYSNMP_MODULE_ID=salixGenericTc, InterfaceIndexOrZero=InterfaceIndexOrZero)
