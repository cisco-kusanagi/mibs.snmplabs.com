#
# PySNMP MIB module SALIX-GENERIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-GENERIC-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:00:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
salixGeneric, = mibBuilder.importSymbols("SALIX-MIB", "salixGeneric")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, iso, ObjectIdentity, Bits, Integer32, IpAddress, Unsigned32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "Integer32", "IpAddress", "Unsigned32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
salixGenericTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 2))
if mibBuilder.loadTexts: salixGenericTc.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixGenericTc.setOrganization('SALIX Technologies')
if mibBuilder.loadTexts: salixGenericTc.setContactInfo('904 Wind River Lane Suite 101 Gaithersburg, MD 20878 (301)-417-0017')
if mibBuilder.loadTexts: salixGenericTc.setDescription('Contains Generic Textual Conventions for use in SALIX products')
class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the InterfaceIndex convention. The latter defines a greater than zero value used to identify an interface or interface sub-layer in the managed system. This extension permits the additional value of zero. the value zero is object-specific and must therefore be defined as part of the description of any object which uses this syntax. Examples of the usage of zero might include situations where interface was unknown, or when none or all interfaces need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("SALIX-GENERIC-TC", salixGenericTc=salixGenericTc, InterfaceIndexOrZero=InterfaceIndexOrZero, PYSNMP_MODULE_ID=salixGenericTc)
