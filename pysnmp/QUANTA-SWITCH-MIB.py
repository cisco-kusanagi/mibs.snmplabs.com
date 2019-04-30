#
# PySNMP MIB module QUANTA-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QUANTA-SWITCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:23:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Counter32, enterprises, Integer32, IpAddress, TimeTicks, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Counter32", "enterprises", "Integer32", "IpAddress", "TimeTicks", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
quanta = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244))
if mibBuilder.loadTexts: quanta.setLastUpdated('200405240000Z')
if mibBuilder.loadTexts: quanta.setOrganization('Quanta Computer Inc.')
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2))
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("QUANTA-SWITCH-MIB", switch=switch, PYSNMP_MODULE_ID=quanta, AgentPortMask=AgentPortMask, quanta=quanta)
