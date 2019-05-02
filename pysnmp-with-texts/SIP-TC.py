#
# PySNMP MIB module SIP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:04:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
sipMIB, = mibBuilder.importSymbols("SIP-MIB-SMI", "sipMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, IpAddress, MibIdentifier, iso, ObjectIdentity, Bits, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 9998, 1))
if mibBuilder.loadTexts: sipTC.setLastUpdated('200007080000Z')
if mibBuilder.loadTexts: sipTC.setOrganization('IETF SIP Working Group, SIP MIB Team')
if mibBuilder.loadTexts: sipTC.setContactInfo('SIP MIB Team email: sip-mib@egroups.com Co-editor Kevin Lingle Cisco Systems, Inc. postal: 7025 Kit Creek Road P.O. Box 14987 Research Triangle Park, NC 27709 Lingle/Maeng/Walker 6 Internet Draft SIP-MIB July, 2000 USA email: klingle@cisco.com phone: +1-919-392-2029 Co-editor Joon Maeng VTEL Corporation postal: 108 Wild Basin Rd. Austin, TX 78746 USA email: joon_maeng@vtel.com phone: +1-512-437-4567 Co-editor Dave Walker SS8 Networks, Inc. postal: 80 Hines Road Kanata, ON K2K 2T8 Canada email: drwalker@ss8networks.com phone: +1 613 592 2100')
if mibBuilder.loadTexts: sipTC.setDescription('Initial version of Session Initiation Protocol (SIP) MIB Textual Conventions module used by other SIP-related MIB Modules.')
class SipServerActions(TextualConvention, Integer32):
    description = 'Lists the possible actions of a SIP network server. A specific action may be requested by a user agent as a Contact parameter in a REGISTER.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("redirect", 1), ("proxy", 2))

mibBuilder.exportSymbols("SIP-TC", sipTC=sipTC, PYSNMP_MODULE_ID=sipTC, SipServerActions=SipServerActions)
