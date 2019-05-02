#
# PySNMP MIB module INCOGNITO-IPCOMMANDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INCOGNITO-IPCOMMANDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:53:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
incognitoProducts, = mibBuilder.importSymbols("INCOGNITO-MIB", "incognitoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, NotificationType, ObjectIdentity, Bits, IpAddress, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "IpAddress", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Integer32", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
incognitoIPCommander = ModuleIdentity((1, 3, 6, 1, 4, 1, 3606, 4, 1))
if mibBuilder.loadTexts: incognitoIPCommander.setLastUpdated('200304151520Z')
if mibBuilder.loadTexts: incognitoIPCommander.setOrganization('Incognito Software Inc.')
if mibBuilder.loadTexts: incognitoIPCommander.setContactInfo('Incognito Software Inc. Customer Service Postal: 1128 Hornby St. Vancouver, BC, Canada V6Z 2L4 Tel: +1 604-688-4332 Fax: +1 604-688-4339 E-Mail: support@incognito.com')
if mibBuilder.loadTexts: incognitoIPCommander.setDescription('')
mibBuilder.exportSymbols("INCOGNITO-IPCOMMANDER-MIB", incognitoIPCommander=incognitoIPCommander, PYSNMP_MODULE_ID=incognitoIPCommander)
