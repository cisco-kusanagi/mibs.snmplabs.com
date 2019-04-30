#
# PySNMP MIB module SALIX-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
salixProducts, salixGeneric, salixRegistrations, salixGroups = mibBuilder.importSymbols("SALIX-MIB", "salixProducts", "salixGeneric", "salixRegistrations", "salixGroups")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, TimeTicks, NotificationType, Counter64, IpAddress, Integer32, Unsigned32, Counter32, MibIdentifier, iso, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter64", "IpAddress", "Integer32", "Unsigned32", "Counter32", "MibIdentifier", "iso", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
salixProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 1))
if mibBuilder.loadTexts: salixProductsMIB.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixProductsMIB.setOrganization('SALIX Technologies')
hne = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 4, 1))
hneAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 4, 2))
hneAgentMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 2158, 4, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hneAgentMajorVersion.setStatus('current')
hneAgentSubVersion = MibScalar((1, 3, 6, 1, 4, 1, 2158, 4, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hneAgentSubVersion.setStatus('current')
itx = ObjectIdentity((1, 3, 6, 1, 4, 1, 2158, 4, 3))
if mibBuilder.loadTexts: itx.setStatus('current')
mibBuilder.exportSymbols("SALIX-PRODUCTS-MIB", hneAgentSubVersion=hneAgentSubVersion, salixProductsMIB=salixProductsMIB, hneAgent=hneAgent, hne=hne, hneAgentMajorVersion=hneAgentMajorVersion, itx=itx, PYSNMP_MODULE_ID=salixProductsMIB)
