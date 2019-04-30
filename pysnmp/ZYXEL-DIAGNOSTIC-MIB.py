#
# PySNMP MIB module ZYXEL-DIAGNOSTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DIAGNOSTIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, IpAddress, Counter64, TimeTicks, NotificationType, ObjectIdentity, ModuleIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "IpAddress", "Counter64", "TimeTicks", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDiagnostic = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95))
if mibBuilder.loadTexts: zyxelDiagnostic.setLastUpdated('201305060000Z')
if mibBuilder.loadTexts: zyxelDiagnostic.setOrganization('Enterprise Solution ZyXEL')
zyxelLocatorLedStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95, 1))
zyLocatorLed = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 95, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLocatorLed.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DIAGNOSTIC-MIB", zyLocatorLed=zyLocatorLed, zyxelDiagnostic=zyxelDiagnostic, zyxelLocatorLedStatus=zyxelLocatorLedStatus, PYSNMP_MODULE_ID=zyxelDiagnostic)
