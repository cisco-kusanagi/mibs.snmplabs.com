#
# PySNMP MIB module NORTEL-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-GENERIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, iso, Unsigned32, Integer32, ModuleIdentity, Counter64, Bits, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "iso", "Unsigned32", "Integer32", "ModuleIdentity", "Counter64", "Bits", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelGenericMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29))
nortelGenericMIBs.setRevisions(('1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nortelGenericMIBs.setRevisionsDescriptions((' The fourth version of this MIB module. Module name changed. Revisions introduced by Shobana Sundaram.', ' The third version of this MIB module. Contact info updated and Revision history added.', ' The second version of this MIB module. Contact info introduced and Revision history added. Object description improved.', ' The first version of this MIB module.',))
if mibBuilder.loadTexts: nortelGenericMIBs.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelGenericMIBs.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortelGenericMIBs.setContactInfo(' Jingdong Liu Postal: Nortel Networks P. O. Box 3511, Station C Ottawa, Ontario CANADA K1Y 4H7 Email: jingdong@nortelnetworks.com')
if mibBuilder.loadTexts: nortelGenericMIBs.setDescription('This module represents the top-level MIB branch for some of the generic MIBs that are common to NortelNetworks products.')
nortelNetworkManagementInterfaceMIBs = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1))
if mibBuilder.loadTexts: nortelNetworkManagementInterfaceMIBs.setStatus('current')
if mibBuilder.loadTexts: nortelNetworkManagementInterfaceMIBs.setDescription("This OID represents the Network Management Interface (NMI) branch for the Nortel Networks's generic MIBs suite. Nortel NMI is an umbrella to include various generic MIBs that can be implemented by Nortel devices to interface to a carrier grade Network Management System (NMS). This branch currently consists of MIBs to support carrier grade alarm surveillance. Characteristics of such a system as applicable to this interface are - reliable and accurate alarm service - capability to summarise currently outstanding alarms - no stuck alarms, no need to age out / manually clear alarms - standards based open interface to alarms For future revisions of the Nortel NMI MIBs, it is mandatory to ensure that the changes are backward compatible. It is very IMPORTANT to follow the SMI rules at RFC 1902 to ensure that no non-backward compatible changes are made as multiple applications use this for various purposes. This MIB is entensible, but the current set of variables cannot be modified. ")
mibBuilder.exportSymbols("NORTEL-GENERIC-MIB", nortelGenericMIBs=nortelGenericMIBs, nortelNetworkManagementInterfaceMIBs=nortelNetworkManagementInterfaceMIBs, PYSNMP_MODULE_ID=nortelGenericMIBs)
