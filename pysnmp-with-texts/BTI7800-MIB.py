#
# PySNMP MIB module BTI7800-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, ModuleIdentity, iso, NotificationType, IpAddress, Unsigned32, ObjectIdentity, enterprises, Counter32, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "iso", "NotificationType", "IpAddress", "Unsigned32", "ObjectIdentity", "enterprises", "Counter32", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bTI7800_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3)).setLabel("bTI7800-MIB")
if mibBuilder.loadTexts: bTI7800_MIB.setLastUpdated('201510081200Z')
if mibBuilder.loadTexts: bTI7800_MIB.setOrganization('BTI Systems Inc.')
if mibBuilder.loadTexts: bTI7800_MIB.setContactInfo('Technical Support BTI Systems Inc. 200-1000 Innovation Dr. Kanata, Ontario, Canada K2K 3E7 (613) 287-1700 support@btisystems.com')
if mibBuilder.loadTexts: bTI7800_MIB.setDescription('BTI7800-MIB original version')
mibBuilder.exportSymbols("BTI7800-MIB", bTI7800_MIB=bTI7800_MIB, PYSNMP_MODULE_ID=bTI7800_MIB)
