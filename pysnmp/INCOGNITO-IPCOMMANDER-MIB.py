#
# PySNMP MIB module INCOGNITO-IPCOMMANDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INCOGNITO-IPCOMMANDER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
incognitoProducts, = mibBuilder.importSymbols("INCOGNITO-MIB", "incognitoProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Integer32, NotificationType, Counter64, ObjectIdentity, IpAddress, MibIdentifier, Bits, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "NotificationType", "Counter64", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
incognitoIPCommander = ModuleIdentity((1, 3, 6, 1, 4, 1, 3606, 4, 1))
if mibBuilder.loadTexts: incognitoIPCommander.setLastUpdated('200304151520Z')
if mibBuilder.loadTexts: incognitoIPCommander.setOrganization('Incognito Software Inc.')
mibBuilder.exportSymbols("INCOGNITO-IPCOMMANDER-MIB", incognitoIPCommander=incognitoIPCommander, PYSNMP_MODULE_ID=incognitoIPCommander)
