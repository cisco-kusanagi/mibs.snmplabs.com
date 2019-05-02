#
# PySNMP MIB module AN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, IpAddress, MibIdentifier, Counter32, Unsigned32, ModuleIdentity, Counter64, NotificationType, TimeTicks, Gauge32, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "IpAddress", "MibIdentifier", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "Integer32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
siemensUnits = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7))
oenProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1))
an = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 2))
xld = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1))
onu = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1))
olt = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 2))
xldOnuSnmVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100))
xldSnmMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xldSnmMibVersion.setStatus('mandatory')
if mibBuilder.loadTexts: xldSnmMibVersion.setDescription(" Version of ONU SNMP MIB. The string is 'V1.0'. ")
xldSnmAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xldSnmAgentVersion.setStatus('mandatory')
if mibBuilder.loadTexts: xldSnmAgentVersion.setDescription(" Version of ONU SNMP agent. The string is 'V1.0'. ")
mibBuilder.exportSymbols("AN-MIB", DisplayString=DisplayString, siemensUnits=siemensUnits, oenProductMibs=oenProductMibs, xldSnmAgentVersion=xldSnmAgentVersion, xldSnmMibVersion=xldSnmMibVersion, an=an, sni=sni, onu=onu, olt=olt, xldOnuSnmVersion=xldOnuSnmVersion, xld=xld)
