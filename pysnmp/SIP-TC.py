#
# PySNMP MIB module SIP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
sipMIB, = mibBuilder.importSymbols("SIP-MIB-SMI", "sipMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, iso, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, IpAddress, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "iso", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 9998, 1))
if mibBuilder.loadTexts: sipTC.setLastUpdated('200007080000Z')
if mibBuilder.loadTexts: sipTC.setOrganization('IETF SIP Working Group, SIP MIB Team')
class SipServerActions(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("redirect", 1), ("proxy", 2))

mibBuilder.exportSymbols("SIP-TC", PYSNMP_MODULE_ID=sipTC, SipServerActions=SipServerActions, sipTC=sipTC)
