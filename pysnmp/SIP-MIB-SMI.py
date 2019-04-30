#
# PySNMP MIB module SIP-MIB-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-MIB-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, Counter32, Counter64, Gauge32, Bits, NotificationType, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, MibIdentifier, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "Gauge32", "Bits", "NotificationType", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "MibIdentifier", "ObjectIdentity", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 9998))
if mibBuilder.loadTexts: sipMIB.setLastUpdated('200007080000Z')
if mibBuilder.loadTexts: sipMIB.setOrganization('IETF SIP Working Group, SIP MIB Team')
mibBuilder.exportSymbols("SIP-MIB-SMI", sipMIB=sipMIB, PYSNMP_MODULE_ID=sipMIB)
