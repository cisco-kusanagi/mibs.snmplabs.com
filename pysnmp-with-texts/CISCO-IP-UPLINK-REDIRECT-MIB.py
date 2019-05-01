#
# PySNMP MIB module CISCO-IP-UPLINK-REDIRECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-UPLINK-REDIRECT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:02:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Bits, Unsigned32, Counter32, Counter64, ObjectIdentity, iso, Integer32, Gauge32, IpAddress, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Bits", "Unsigned32", "Counter32", "Counter64", "ObjectIdentity", "iso", "Integer32", "Gauge32", "IpAddress", "TimeTicks", "NotificationType")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoIpUplinkRedirectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 191))
ciscoIpUplinkRedirectMIB.setRevisions(('2001-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setLastUpdated('200101220000Z')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cat2948g-l3@cisco.com')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setDescription('This MIB module is for the configuration of Cisco IP Uplink Redirect feature.')
ciscoIpUplinkRedirectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 1))
ciurStartupStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciurStartupStatus.setStatus('current')
if mibBuilder.loadTexts: ciurStartupStatus.setDescription('The indication of whether IP Uplink Redirect feature will be enabled or disabled on this entity after reboot. IP uplink redirect enables traffic between Fast Ethernet interfaces to be switched through the Gigabit Ethernet interface. Then ACLs applied on the Gigabit Ethernet interface filter traffic switched between Fast Ethernet interfaces. Once the IP Uplink Redirect feature is enabled and saved, the switch has to be rebooted for it to take effect.')
ciurOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciurOperStatus.setStatus('current')
if mibBuilder.loadTexts: ciurOperStatus.setDescription('Indicates whether or not IP Uplink Redirect is currently operational on this entity.')
ciscoIpUplinkRedirectMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 2))
ciscoIpUplinkRedirectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3))
ciscoIpUplinkRedirectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1))
ciscoIpUplinkRedirectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2))
ciscoIpUplinkRedirectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciscoIpUplinkRedirectMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBCompliance = ciscoIpUplinkRedirectMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIBCompliance.setDescription('The compliance statement for the Cisco L3 Switch/Router IP Uplink Redirect group.')
ciscoIpUplinkRedirectMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurStartupStatus"), ("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBGroup = ciscoIpUplinkRedirectMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIBGroup.setDescription('The Object Group for IP Uplink Redirect')
mibBuilder.exportSymbols("CISCO-IP-UPLINK-REDIRECT-MIB", ciscoIpUplinkRedirectMIBGroup=ciscoIpUplinkRedirectMIBGroup, ciscoIpUplinkRedirectMIBNotificationPrefix=ciscoIpUplinkRedirectMIBNotificationPrefix, ciscoIpUplinkRedirectMIBCompliances=ciscoIpUplinkRedirectMIBCompliances, ciurStartupStatus=ciurStartupStatus, ciscoIpUplinkRedirectMIBObjects=ciscoIpUplinkRedirectMIBObjects, ciscoIpUplinkRedirectMIBConformance=ciscoIpUplinkRedirectMIBConformance, ciscoIpUplinkRedirectMIBCompliance=ciscoIpUplinkRedirectMIBCompliance, ciscoIpUplinkRedirectMIB=ciscoIpUplinkRedirectMIB, ciurOperStatus=ciurOperStatus, ciscoIpUplinkRedirectMIBGroups=ciscoIpUplinkRedirectMIBGroups, PYSNMP_MODULE_ID=ciscoIpUplinkRedirectMIB)
