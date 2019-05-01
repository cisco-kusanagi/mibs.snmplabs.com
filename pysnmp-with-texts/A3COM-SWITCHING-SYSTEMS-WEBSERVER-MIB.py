#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:08:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter64, Unsigned32, Gauge32, NotificationType, IpAddress, MibIdentifier, ModuleIdentity, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "Unsigned32", "Gauge32", "NotificationType", "IpAddress", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
switchingSystemsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29))
a3ComSwitchingSystemsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4))
a3ComWebConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 24))
a3ComWebConfigHelpServer = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigHelpServer.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComWebConfigHelpServer.setDescription("The server's URL where help pages are taken from upon http requests. Example: http://0.0.0.0/3Com/help")
a3ComWebConfigEmailServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComWebConfigEmailServerAddress.setDescription("The mail server that you want the system to use for mailing status changes to the addresses specified under a3ComWebConfigEmailAddresses. This object may be an ip address or a machine's name assuming the managed device has client DNS capabilities.")
a3ComWebConfigEmailAddresses = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailAddresses.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComWebConfigEmailAddresses.setDescription('The email addresses to which you wish to mail status changes, adding a semicolon after each address, including cases where only one address is specified.')
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB", a3ComSwitchingSystemsMib=a3ComSwitchingSystemsMib, a3ComWebConfigEmailServerAddress=a3ComWebConfigEmailServerAddress, a3ComWebConfigEmailAddresses=a3ComWebConfigEmailAddresses, a3ComWebConfigHelpServer=a3ComWebConfigHelpServer, switchingSystemsMibs=switchingSystemsMibs, a3ComWebConfig=a3ComWebConfig, a3Com=a3Com)
