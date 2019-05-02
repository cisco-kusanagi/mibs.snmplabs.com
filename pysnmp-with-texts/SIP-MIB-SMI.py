#
# PySNMP MIB module SIP-MIB-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-MIB-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:04:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, iso, Integer32, ObjectIdentity, IpAddress, TimeTicks, Gauge32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, mib_2, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "mib-2", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 9998))
if mibBuilder.loadTexts: sipMIB.setLastUpdated('200007080000Z')
if mibBuilder.loadTexts: sipMIB.setOrganization('IETF SIP Working Group, SIP MIB Team')
if mibBuilder.loadTexts: sipMIB.setContactInfo('SIP MIB Team email: sip-mib@egroups.com Co-editor Kevin Lingle Cisco Systems, Inc. postal: 7025 Kit Creek Road Lingle/Maeng/Walker 5 Internet Draft SIP-MIB July, 2000 P.O. Box 14987 Research Triangle Park, NC 27709 USA email: klingle@cisco.com phone: +1-919-392-2029 Co-editor Joon Maeng VTEL Corporation postal: 108 Wild Basin Rd. Austin, TX 78746 USA email: joon_maeng@vtel.com phone: +1-512-437-4567 Co-editor Dave Walker SS8 Networks, Inc. postal: 80 Hines Road Kanata, ON K2K 2T8 Canada email: drwalker@ss8networks.com phone: +1 613 592 2100')
if mibBuilder.loadTexts: sipMIB.setDescription('Initial version of Session Initiation Protocol (SIP) MIB module that defines base OID for all other SIP-related MIB Modules.')
mibBuilder.exportSymbols("SIP-MIB-SMI", sipMIB=sipMIB, PYSNMP_MODULE_ID=sipMIB)
