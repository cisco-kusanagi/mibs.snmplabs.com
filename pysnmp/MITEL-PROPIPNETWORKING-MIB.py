#
# PySNMP MIB module MITEL-PROPIPNETWORKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-PROPIPNETWORKING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, NotificationType, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "NotificationType", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "Gauge32", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelIpNetRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpNetRouter.setRevisions(('2003-03-24 10:31', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelIpNetRouter.setLastUpdated('200303241031Z')
if mibBuilder.loadTexts: mitelIpNetRouter.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mibBuilder.exportSymbols("MITEL-PROPIPNETWORKING-MIB", mitelIpNetRouter=mitelIpNetRouter, mitelPropIpNetworking=mitelPropIpNetworking, mitelProprietary=mitelProprietary, mitel=mitel, PYSNMP_MODULE_ID=mitelIpNetRouter)
