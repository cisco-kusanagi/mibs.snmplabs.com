#
# PySNMP MIB module AN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Integer32, Bits, iso, Counter64, MibIdentifier, enterprises, Unsigned32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "iso", "Counter64", "MibIdentifier", "enterprises", "Unsigned32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
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
xldSnmAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xldSnmAgentVersion.setStatus('mandatory')
mibBuilder.exportSymbols("AN-MIB", xld=xld, xldOnuSnmVersion=xldOnuSnmVersion, xldSnmAgentVersion=xldSnmAgentVersion, DisplayString=DisplayString, oenProductMibs=oenProductMibs, onu=onu, xldSnmMibVersion=xldSnmMibVersion, sni=sni, siemensUnits=siemensUnits, an=an, olt=olt)
