#
# PySNMP MIB module BTI7800-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, NotificationType, MibIdentifier, ObjectIdentity, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ModuleIdentity, Bits, Gauge32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "MibIdentifier", "ObjectIdentity", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ModuleIdentity", "Bits", "Gauge32", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bTI7800_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3)).setLabel("bTI7800-MIB")
if mibBuilder.loadTexts: bTI7800_MIB.setLastUpdated('201510081200Z')
if mibBuilder.loadTexts: bTI7800_MIB.setOrganization('BTI Systems Inc.')
mibBuilder.exportSymbols("BTI7800-MIB", PYSNMP_MODULE_ID=bTI7800_MIB, bTI7800_MIB=bTI7800_MIB)
