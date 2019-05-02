#
# PySNMP MIB module PDN-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
pdn_dns, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-dns")
DomainName, DNSServerType = mibBuilder.importSymbols("PDN-TC", "DomainName", "DNSServerType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, Bits, ModuleIdentity, Gauge32, Unsigned32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks", "IpAddress", "NotificationType")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
pdnDNSMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1))
pdnDNSMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 2))
devDNSDefaultDomainName = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 1), DomainName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSDefaultDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSDefaultDomainName.setDescription('the object allows the NMS to configure the default domain name for the device')
devDNSRetryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSRetryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSRetryTimeout.setDescription('the object allows the NMS to configure in seconds the time to wait for a response from a DNS server. The default value for this object is 5')
devDNSMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSMaxRetries.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSMaxRetries.setDescription('the object allows the NMS to configure the number of maximum number of retires by the device before giving up or trying one of the secondary DNS servers if they have been configured. The default value for this object is 2')
devDNSServerTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4), )
if mibBuilder.loadTexts: devDNSServerTable.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSServerTable.setDescription('A Table that contains information about the DNS server IP addresses')
devDNSServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1), ).setIndexNames((0, "PDN-DNS-MIB", "devDNSServerIP"))
if mibBuilder.loadTexts: devDNSServerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSServerEntry.setDescription('A Table that contains information about the DNS server IP addresses')
devDNSServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDNSServerIP.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSServerIP.setDescription('This Objects allows an NMS to configure a DNS server IP address Default value is 1')
devDNSServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 2), DNSServerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSServerType.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSServerType.setDescription('This Objects allows an NMS to specify whether the Server IP address is the primary DNS server or the secondary DNS server. Only One Primary DNS server is allowed to be configured.')
devDNSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDNSRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: devDNSRowStatus.setDescription('Use CreateAndGo to Create a new object. use Destroy to remove an entry from this table')
devHostMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5), )
if mibBuilder.loadTexts: devHostMappingTable.setStatus('mandatory')
if mibBuilder.loadTexts: devHostMappingTable.setDescription('A Table that contains information about host names for devices')
devHostMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1), ).setIndexNames((0, "PDN-DNS-MIB", "devHostMappingIpAddress"))
if mibBuilder.loadTexts: devHostMappingEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devHostMappingEntry.setDescription('An entry that contains information about a device host name')
devHostMappingIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devHostMappingIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: devHostMappingIpAddress.setDescription('This object contains the IP Address of the host')
devHostMappingHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devHostMappingHostName.setStatus('mandatory')
if mibBuilder.loadTexts: devHostMappingHostName.setDescription('This object contains the name of the host')
devHostMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devHostMappingRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: devHostMappingRowStatus.setDescription('This object is used to create or delete a row from the table')
mibBuilder.exportSymbols("PDN-DNS-MIB", devDNSServerEntry=devDNSServerEntry, devDNSRowStatus=devDNSRowStatus, devDNSServerType=devDNSServerType, pdnDNSMIBObjects=pdnDNSMIBObjects, devHostMappingIpAddress=devHostMappingIpAddress, devHostMappingHostName=devHostMappingHostName, pdnDNSMIBTraps=pdnDNSMIBTraps, devDNSMaxRetries=devDNSMaxRetries, devDNSServerIP=devDNSServerIP, devHostMappingTable=devHostMappingTable, devDNSRetryTimeout=devDNSRetryTimeout, devHostMappingEntry=devHostMappingEntry, devHostMappingRowStatus=devHostMappingRowStatus, devDNSServerTable=devDNSServerTable, devDNSDefaultDomainName=devDNSDefaultDomainName)
