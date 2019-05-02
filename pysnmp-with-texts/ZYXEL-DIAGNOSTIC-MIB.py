#
# PySNMP MIB module ZYXEL-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DIAGNOSTIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:49:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, Gauge32, TimeTicks, NotificationType, IpAddress, Counter32, Integer32, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "Gauge32", "TimeTicks", "NotificationType", "IpAddress", "Counter32", "Integer32", "MibIdentifier", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDiagnostic = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95))
if mibBuilder.loadTexts: zyxelDiagnostic.setLastUpdated('201305060000Z')
if mibBuilder.loadTexts: zyxelDiagnostic.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelDiagnostic.setContactInfo('')
if mibBuilder.loadTexts: zyxelDiagnostic.setDescription('The subtree for diagnostic')
zyxelLocatorLedStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95, 1))
zyLocatorLed = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLocatorLed.setStatus('current')
if mibBuilder.loadTexts: zyLocatorLed.setDescription('Locator LED blinking time in minutes.')
mibBuilder.exportSymbols("ZYXEL-DIAGNOSTIC-MIB", zyLocatorLed=zyLocatorLed, PYSNMP_MODULE_ID=zyxelDiagnostic, zyxelLocatorLedStatus=zyxelLocatorLedStatus, zyxelDiagnostic=zyxelDiagnostic)
