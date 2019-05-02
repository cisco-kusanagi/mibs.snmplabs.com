#
# PySNMP MIB module MITEL-PROPIPNETWORKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-PROPIPNETWORKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Counter64, ObjectIdentity, IpAddress, NotificationType, MibIdentifier, Counter32, Gauge32, iso, enterprises, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "Gauge32", "iso", "enterprises", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelIpNetRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpNetRouter.setRevisions(('2003-03-24 10:31', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpNetRouter.setRevisionsDescriptions(('Convert to SMIv2', 'IP Networking MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpNetRouter.setLastUpdated('200303241031Z')
if mibBuilder.loadTexts: mitelIpNetRouter.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpNetRouter.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpNetRouter.setDescription('The MITEL IP Networking module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mibBuilder.exportSymbols("MITEL-PROPIPNETWORKING-MIB", PYSNMP_MODULE_ID=mitelIpNetRouter, mitelPropIpNetworking=mitelPropIpNetworking, mitelProprietary=mitelProprietary, mitel=mitel, mitelIpNetRouter=mitelIpNetRouter)
