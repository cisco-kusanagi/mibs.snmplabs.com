#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Bits, TimeTicks, Gauge32, IpAddress, MibIdentifier, ModuleIdentity, Counter64, iso, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Bits", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "iso", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
switchingSystemsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29))
a3ComSwitchingSystemsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4))
a3ComWebConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 24))
a3ComWebConfigHelpServer = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigHelpServer.setStatus('mandatory')
a3ComWebConfigEmailServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailServerAddress.setStatus('mandatory')
a3ComWebConfigEmailAddresses = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailAddresses.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB", a3ComSwitchingSystemsMib=a3ComSwitchingSystemsMib, a3ComWebConfigEmailServerAddress=a3ComWebConfigEmailServerAddress, switchingSystemsMibs=switchingSystemsMibs, a3ComWebConfigEmailAddresses=a3ComWebConfigEmailAddresses, a3Com=a3Com, a3ComWebConfigHelpServer=a3ComWebConfigHelpServer, a3ComWebConfig=a3ComWebConfig)
