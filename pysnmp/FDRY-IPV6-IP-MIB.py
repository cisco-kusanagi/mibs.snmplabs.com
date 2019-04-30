#
# PySNMP MIB module FDRY-IPV6-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-IPV6-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
RtrStatus, = mibBuilder.importSymbols("FOUNDRY-SN-IP-MIB", "RtrStatus")
fdryIpv6, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryIpv6")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Integer32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, IpAddress, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fdryIpv6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1))
fdryIpv6MIB.setRevisions(('2010-07-26 00:00', '2010-05-06 00:00',))
if mibBuilder.loadTexts: fdryIpv6MIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryIpv6MIB.setOrganization('Brocade Communications Systems, Inc.')
fdryIpv6GlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1))
fdryIpv6LoadShare = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 1), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShare.setStatus('current')
fdryIpv6LoadShareNumOfPaths = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 17, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpv6LoadShareNumOfPaths.setStatus('current')
mibBuilder.exportSymbols("FDRY-IPV6-IP-MIB", fdryIpv6GlobalObjects=fdryIpv6GlobalObjects, fdryIpv6LoadShare=fdryIpv6LoadShare, PYSNMP_MODULE_ID=fdryIpv6MIB, fdryIpv6LoadShareNumOfPaths=fdryIpv6LoadShareNumOfPaths, fdryIpv6MIB=fdryIpv6MIB)
