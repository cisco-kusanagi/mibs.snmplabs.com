#
# PySNMP MIB module HPOV-SNMPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPOV-SNMPSEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, NotificationType, enterprises, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32, Counter32, TimeTicks, IpAddress, Counter64, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "enterprises", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32", "Counter32", "TimeTicks", "IpAddress", "Counter64", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
class OVTDAddress(TextualConvention, OctetString):
    reference = 'RFC 1906, Transport Mappings for SNMP Version 2'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

hpOVSNMPSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 5))
hpOVSecureTarget = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 5, 1), OVTDAddress())
if mibBuilder.loadTexts: hpOVSecureTarget.setStatus('current')
mibBuilder.exportSymbols("HPOV-SNMPSEC-MIB", hpOVSNMPSecurity=hpOVSNMPSecurity, hpOVSecureTarget=hpOVSecureTarget, OVTDAddress=OVTDAddress, nm=nm, hp=hp, openView=openView)
